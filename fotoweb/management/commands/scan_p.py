from datetime import datetime, timedelta
import re
import os
import zlib
import base64
from dateutil import parser
from io import BytesIO
from iptcinfo3 import IPTCInfo

from pcloud import PyCloud
from imagekitio import ImageKit
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import connections

from fotoweb.models import *

import logging
logger = logging.getLogger(__name__)

imagekits = []

#if os.environ.get('IMAGEKIT_PRIVATE_KEY'):
#    imagekit = ImageKit(
#        private_key=os.environ['IMAGEKIT_PRIVATE_KEY'],
#        public_key=os.environ['IMAGEKIT_PUBLIC_KEY'],
#        url_endpoint=os.environ['IMAGEKIT_URL_ENDPOINT'],
#    )
#    imagekits.append(imagekit)

if os.environ.get('IMAGEKIT_PRIVATE_KEY_1'):
    imagekit = ImageKit(
        private_key=os.environ['IMAGEKIT_PRIVATE_KEY_1'],
        public_key=os.environ['IMAGEKIT_PUBLIC_KEY_1'],
        url_endpoint=os.environ['IMAGEKIT_URL_ENDPOINT_1'],
    )
    imagekits.append(imagekit)

if os.environ.get('IMAGEKIT_PRIVATE_KEY_2'):
    imagekit = ImageKit(
        private_key=os.environ['IMAGEKIT_PRIVATE_KEY_2'],
        public_key=os.environ['IMAGEKIT_PUBLIC_KEY_2'],
        url_endpoint=os.environ['IMAGEKIT_URL_ENDPOINT_2'],
    )
    imagekits.append(imagekit)



pc = PyCloud(os.environ['P_USERNAME'], os.environ['P_PASSWORD'])

start_dir = '/Gellifique/VALYA/C1/foto'
#start_dir = '/Gellifique/VALYA/C1/foto/Twilight near Faro de Cullera'

imgk_start_dir = '/C1/foto'
imgk_nostore_dir = '/Gellifique/VALYA'
cnt = 0

def open_dir(dir,albums_needs_cover):
    global cnt

    print ('dir:',dir)
    ff = pc.listfolder(path=dir)
    #print(ff)

    for f in sorted(ff['metadata']['contents'],key=lambda file: file['path']):
        if f['isfolder']:
            need_cover = None
            if not 'JPEG-2048' in f['path'] and not 'JPEG-Full-size' in f['path']:
                path = f['path'].replace(imgk_nostore_dir,'')
                path = path.replace(' ','_')
                path = re.sub(r'[^/_0-9A-Za-z\-.]','_',path)
                path = path.replace('__','_')
                title = path.replace(imgk_start_dir+'/','')
                title = re.sub('/[^/]*2048[^/]*','',title)
                print('>>>',path,title)
                try:
                    album = Album.objects.get(path=path)
                    need_cover = album if not album.cover else None
                except Album.DoesNotExist:
                    album = Album(path=path,title=title)
                    album.save()
                    need_cover = album

            if need_cover:
                albums_needs_cover.append(need_cover)

                print ('folders need cover:',albums_needs_cover)


            open_dir (f['path'],albums_needs_cover)
        else:
            if f['contenttype']=='image/jpeg' and 'JPEG-2048' in f['path']:
                cnt += 1
                #print(f)
                fdt = parser.parse(f['created'])
                fdtm = parser.parse(f['modified'])
                new_dir = dir.replace(imgk_nostore_dir,'')
                new_dir = new_dir.replace(' ','_')
                new_dir = re.sub(r'[^/_0-9A-Za-z\-.]','_',new_dir)
                new_dir = new_dir.replace('__','_')

                fn = os.path.basename(f['path'].replace(' ','_'))

                options = ListAndSearchFileRequestOptions(
                    path=new_dir,
                    search_query=f"name='{fn}'"
                )

                #res = imagekit.list_files({'path':new_dir,'name':fn})
                res = imagekit.list_files(options=options)
                #if res['error']:
                #    print ('ERROR',res)

                if res.list and res.list[0]:
                    #print('dates:',f['path'],parser.parse(res.list[0].updated_at),fdt,fdtm)
                    print('dirs:',f['path'],new_dir,zlib.crc32(bytes(new_dir,'utf8')) % len(imagekits))
                    #print(res['response'][0])

                if not res.list or parser.parse(res.list[0].updated_at)<fdt or parser.parse(res.list[0].updated_at)<fdtm:
                #if not res['response'] or parser.parse(res['response'][0]['updatedAt'])<fdt or parser.parse(res['response'][0]['updatedAt'])<fdtm:
                #if not res['response']:
                    #fd = pc.file_open(path=f['path'],flags=os.O_BINARY)
                    fd = pc.file_open(path=f['path'],flags=os.O_RDONLY)
                    data = pc.file_read(fd=fd['fd'],count=1024*1024*100)
                    print ('len=',len(data))
                    iptc = IPTCInfo(BytesIO(data),inp_charset='utf_8',out_charset='utf_8')
                    print (iptc)

                    provider = 'aws';

                    options = UploadFileRequestOptions(
                        use_unique_file_name=False,
                        folder=new_dir,
                    )

                    upload = imagekit.upload(
                            file=base64.b64encode(data),
                            file_name=fn,
                            options=options
                    )
                    print("Upload binary", upload)
                    pc.file_close(fd=fd)

                    try:
                        img = Image.objects.get(name=upload.name)
                    except Image.DoesNotExist:
                        img = Image(name=upload.name)

                    img.path=upload.file_path
                    img.url=upload.url
                    if not img.title: img.title = iptc['headline']
                    if not img.description: img.description = iptc['caption/abstract']
                    if not img.tags: img.tags = ', '.join(iptc['keywords'])

                    #if not img.aws_tags and upload['response']['AITags']:
                    #    tags = []
                    #    for tag in upload['response']['AITags']:
                    #        if tag['source']==f"{provider}-auto-tagging":
                    #            print (tag)
                    #            tags.append(tag['name'])

                    #    if tags:
                    #        img.aws_tags = ','.join(tags)

                    img.save()
                    print('ID:',img.id)

                    if albums_needs_cover:
                        print ('files - cover:',albums_needs_cover)
                        for album_needs_cover in albums_needs_cover:
                            album_needs_cover.cover = img.url
                            album_needs_cover.save()
                        albums_needs_cover.clear()

                else:
                    pass
                    if albums_needs_cover:
                        print ('files - cover:',albums_needs_cover)
                        for album_needs_cover in albums_needs_cover:
                            #album_needs_cover.cover = res['response'][0]['url']
                            album_needs_cover.cover = res.list[0].url
                            album_needs_cover.save()
                        albums_needs_cover.clear()




class Command(BaseCommand):
    help = 'scan_p'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print (self.help)
        logger.info(self.help)

        open_dir(start_dir,[])

        print ("DONE!")
        logger.error("DONE - %s!",self.help,)





