# Generated by Django 3.2.7 on 2021-12-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotoweb', '0008_alter_album_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.CharField(blank=True, max_length=100, unique=False, verbose_name='slug'),
        ),
    ]