# Generated by Django 3.2.7 on 2021-11-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotoweb', '0004_auto_20211108_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='no_show',
            field=models.BooleanField(default=False, verbose_name='no show'),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated_dt'),
        ),
    ]
