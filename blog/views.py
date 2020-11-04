import re
from django.utils import timezone
from django.views import generic

from .models import *


class ListView(generic.ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(
            blog_start_dt__lte=timezone.now(),blog=True
        ).order_by('-blog_start_dt')[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['post'] = context['post_list'][0]

        n = 0
        for p in context['post_list']:
            if n>0:
                print(p.text)

                pics = re.finditer(r'\!\[\]\(',p.text)

                pos = [pic.start() for pic in pics]

                print (pos[1])

                print(p.text[0:pos[1]])

                p.text = p.text[0:pos[1]]

                p.read_more = True

                #print (pics[1].span())

            n += 1

        context['breadcrumb'] = re.sub(r'[^\x00-\x7F]',' ', context['post'].title)
        return context        

class PostView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['breadcrumb'] = re.sub(r'[^\x00-\x7F]',' ', context['post'].title)
        return context        



