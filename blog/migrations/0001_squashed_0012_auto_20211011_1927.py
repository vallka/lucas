# Generated by Django 4.1 on 2024-03-14 20:22

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    replaces = [('blog', '0001_initial'), ('blog', '0002_category'), ('blog', '0003_category_is_default'), ('blog', '0004_post_category'), ('blog', '0005_auto_20200828_1501'), ('blog', '0006_auto_20201106_1041'), ('blog', '0007_auto_20201106_1042'), ('blog', '0008_post_email_status'), ('blog', '0009_auto_20210225_2136'), ('blog', '0010_auto_20210225_2142'), ('blog', '0011_auto_20210919_1308'), ('blog', '0012_auto_20211011_1927')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Category')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Slug')),
                ('is_default', models.BooleanField(default=False, verbose_name='Default Category')),
            ],
            options={
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, default='', verbose_name='Meta Description')),
                ('keywords', models.TextField(blank=True, default='', verbose_name='Meta Keywords')),
                ('json_ld', models.TextField(blank=True, default='', verbose_name='script ld+json')),
                ('text', markdownx.models.MarkdownxField(blank=True, verbose_name='Text')),
                ('category', models.ManyToManyField(to='blog.category')),
                ('blog', models.BooleanField(default=False, verbose_name='Publish to blog')),
                ('blog_start_dt', models.DateTimeField(blank=True, null=True, verbose_name='Publish Date/Time')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date/Time')),
                ('email', models.BooleanField(default=False, verbose_name='Send as newsletter to UK customers')),
                ('email_send_dt', models.DateTimeField(blank=True, null=True, verbose_name='Send Date/Time')),
                ('updated_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date/Time')),
                ('email_status', models.IntegerField(choices=[(0, 'None'), (1, 'Sending'), (2, 'Sent')], default=0)),
                ('title_bgcolor', models.CharField(blank=True, default='#eeeeee', max_length=20, verbose_name='Title Bg Color')),
                ('title_color', models.CharField(blank=True, default='#232323', max_length=20, verbose_name='Title Color')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]