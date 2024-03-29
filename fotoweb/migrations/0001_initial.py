# Generated by Django 3.1.2 on 2021-09-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('path', models.CharField(max_length=200, unique=True, verbose_name='path')),
                ('url', models.CharField(max_length=200, unique=True, verbose_name='url')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_dt')),
                ('updated_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='created_dt')),
                ('mykeyworder_tags', models.TextField(blank=True, null=True, verbose_name='mykeyworder tags')),
                ('adobe_tags', models.TextField(blank=True, null=True, verbose_name='adobe tags')),
                ('google_tags', models.TextField(blank=True, null=True, verbose_name='goggle tags')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('tags', models.TextField(blank=True, null=True, verbose_name='tags')),
                ('instagram', models.BooleanField(default=False, verbose_name='instagram')),
                ('instagram_dt', models.DateTimeField(blank=True, null=True, verbose_name='instagram_dt')),
                ('instagram_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='instagram_code')),
                ('adobe', models.BooleanField(default=False, verbose_name='adobe')),
                ('adobe_dt', models.DateTimeField(blank=True, null=True, verbose_name='adobe_dt')),
                ('shutter', models.BooleanField(default=False, verbose_name='shutter')),
                ('shutter_dt', models.DateTimeField(blank=True, null=True, verbose_name='shutter_dt')),
            ],
        ),
    ]
