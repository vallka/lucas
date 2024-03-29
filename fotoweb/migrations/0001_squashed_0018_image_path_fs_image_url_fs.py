# Generated by Django 4.1 on 2024-03-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('fotoweb', '0001_initial'), ('fotoweb', '0002_auto_20210919_1725'), ('fotoweb', '0003_auto_20211011_1927'), ('fotoweb', '0004_auto_20211108_2231'), ('fotoweb', '0005_auto_20211121_1810'), ('fotoweb', '0006_album'), ('fotoweb', '0007_album_cover'), ('fotoweb', '0008_alter_album_cover'), ('fotoweb', '0009_album_slug'), ('fotoweb', '0010_alter_album_slug'), ('fotoweb', '0011_image_aws_tags'), ('fotoweb', '0012_alter_image_title'), ('fotoweb', '0013_album_level'), ('fotoweb', '0014_auto_20220121_2159'), ('fotoweb', '0015_image_private'), ('fotoweb', '0016_image_shutter_url'), ('fotoweb', '0017_alter_image_title'), ('fotoweb', '0018_image_path_fs_image_url_fs')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200, unique=True, verbose_name='path')),
                ('no_show', models.BooleanField(default=False, verbose_name='no show')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_dt')),
                ('updated_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_dt')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('position', models.IntegerField(blank=True, default=0, verbose_name='position')),
                ('cover', models.CharField(blank=True, default='', max_length=200, verbose_name='cover')),
                ('slug', models.CharField(blank=True, max_length=100, unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('path', models.CharField(max_length=200, unique=True, verbose_name='path')),
                ('url', models.CharField(max_length=200, unique=True, verbose_name='url')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_dt')),
                ('updated_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_dt')),
                ('mykeyworder_tags', models.TextField(blank=True, null=True, verbose_name='mykeyworder tags')),
                ('adobe_tags', models.TextField(blank=True, null=True, verbose_name='adobe tags')),
                ('google_tags', models.TextField(blank=True, null=True, verbose_name='goggle tags')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('tags', models.TextField(blank=True, null=True, verbose_name='tags')),
                ('instagram', models.BooleanField(default=False, verbose_name='instagram')),
                ('instagram_dt', models.DateTimeField(blank=True, null=True, verbose_name='instagram_dt')),
                ('instagram_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='instagram_code')),
                ('adobe', models.BooleanField(default=False, verbose_name='adobe')),
                ('adobe_dt', models.DateTimeField(blank=True, null=True, verbose_name='adobe_dt')),
                ('shutter', models.BooleanField(default=False, verbose_name='shutter')),
                ('shutter_dt', models.DateTimeField(blank=True, null=True, verbose_name='shutter_dt')),
                ('shutter_tags', models.TextField(blank=True, null=True, verbose_name='shutter tags')),
                ('editorial', models.BooleanField(default=False, verbose_name='editorial')),
                ('shutter_cat1', models.CharField(choices=[('', ''), ('Abstract', 'Abstract'), ('Animals/Wildlife', 'Animals/Wildlife'), ('Backgrounds/Textures', 'Backgrounds/Textures'), ('Beauty/Fashion', 'Beauty/Fashion'), ('Buildings/Landmarks', 'Buildings/Landmarks'), ('Business/Finance', 'Business/Finance'), ('Celebrities', 'Celebrities'), ('Education', 'Education'), ('Food and Drink', 'Food and Drink'), ('Healthcare/Medical', 'Healthcare/Medical'), ('Holidays', 'Holidays'), ('Industrial', 'Industrial'), ('Interiors', 'Interiors'), ('Miscellaneous', 'Miscellaneous'), ('Objects', 'Objects'), ('Parks/Outdoor', 'Parks/Outdoor'), ('People', 'People'), ('Religion', 'Religion'), ('Science', 'Science'), ('Signs/Symbols', 'Signs/Symbols'), ('Sports/Recreation', 'Sports/Recreation'), ('Technology', 'Technology'), ('The Arts', 'The Arts'), ('Vintage', 'Vintage')], default='Buildings/Landmarks', max_length=50)),
                ('shutter_cat2', models.CharField(choices=[('', ''), ('Abstract', 'Abstract'), ('Animals/Wildlife', 'Animals/Wildlife'), ('Backgrounds/Textures', 'Backgrounds/Textures'), ('Beauty/Fashion', 'Beauty/Fashion'), ('Buildings/Landmarks', 'Buildings/Landmarks'), ('Business/Finance', 'Business/Finance'), ('Celebrities', 'Celebrities'), ('Education', 'Education'), ('Food and Drink', 'Food and Drink'), ('Healthcare/Medical', 'Healthcare/Medical'), ('Holidays', 'Holidays'), ('Industrial', 'Industrial'), ('Interiors', 'Interiors'), ('Miscellaneous', 'Miscellaneous'), ('Objects', 'Objects'), ('Parks/Outdoor', 'Parks/Outdoor'), ('People', 'People'), ('Religion', 'Religion'), ('Science', 'Science'), ('Signs/Symbols', 'Signs/Symbols'), ('Sports/Recreation', 'Sports/Recreation'), ('Technology', 'Technology'), ('The Arts', 'The Arts'), ('Vintage', 'Vintage')], default='Parks/Outdoor', max_length=50)),
                ('no_show', models.BooleanField(default=False, verbose_name='no show')),
                ('aws_tags', models.TextField(blank=True, null=True, verbose_name='aws tags')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='level',
            field=models.IntegerField(default=0, verbose_name='level'),
        ),
        migrations.AddField(
            model_name='image',
            name='pexels',
            field=models.BooleanField(default=False, verbose_name='pexels'),
        ),
        migrations.AddField(
            model_name='image',
            name='pexels_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='pexels_dt'),
        ),
        migrations.AddField(
            model_name='image',
            name='pexels_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pexels_url'),
        ),
        migrations.AddField(
            model_name='image',
            name='rasfocus',
            field=models.BooleanField(default=False, verbose_name='rasfocus'),
        ),
        migrations.AddField(
            model_name='image',
            name='rasfocus_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='rasfocus_dt'),
        ),
        migrations.AddField(
            model_name='image',
            name='rasfocus_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='rasfocus_url'),
        ),
        migrations.AddField(
            model_name='image',
            name='private',
            field=models.BooleanField(default=False, verbose_name='private'),
        ),
        migrations.AddField(
            model_name='image',
            name='shutter_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='shutter_url'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='image',
            name='path_fs',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='path'),
        ),
        migrations.AddField(
            model_name='image',
            name='url_fs',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='url'),
        ),
    ]
