# Generated by Django 3.2.7 on 2021-11-08 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotoweb', '0003_auto_20211011_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='editorial',
            field=models.BooleanField(default=False, verbose_name='editorial'),
        ),
        migrations.AddField(
            model_name='image',
            name='shutter_cat1',
            field=models.CharField(choices=[('', ''), ('Abstract', 'Abstract'), ('Animals/Wildlife', 'Animals/Wildlife'), ('Backgrounds/Textures', 'Backgrounds/Textures'), ('Beauty/Fashion', 'Beauty/Fashion'), ('Buildings/Landmarks', 'Buildings/Landmarks'), ('Business/Finance', 'Business/Finance'), ('Celebrities', 'Celebrities'), ('Education', 'Education'), ('Food and Drink', 'Food and Drink'), ('Healthcare/Medical', 'Healthcare/Medical'), ('Holidays', 'Holidays'), ('Industrial', 'Industrial'), ('Interiors', 'Interiors'), ('Miscellaneous', 'Miscellaneous'), ('Objects', 'Objects'), ('Parks/Outdoor', 'Parks/Outdoor'), ('People', 'People'), ('Religion', 'Religion'), ('Science', 'Science'), ('Signs/Symbols', 'Signs/Symbols'), ('Sports/Recreation', 'Sports/Recreation'), ('Technology', 'Technology'), ('The Arts', 'The Arts'), ('Vintage', 'Vintage')], default='Buildings/Landmarks', max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='shutter_cat2',
            field=models.CharField(choices=[('', ''), ('Abstract', 'Abstract'), ('Animals/Wildlife', 'Animals/Wildlife'), ('Backgrounds/Textures', 'Backgrounds/Textures'), ('Beauty/Fashion', 'Beauty/Fashion'), ('Buildings/Landmarks', 'Buildings/Landmarks'), ('Business/Finance', 'Business/Finance'), ('Celebrities', 'Celebrities'), ('Education', 'Education'), ('Food and Drink', 'Food and Drink'), ('Healthcare/Medical', 'Healthcare/Medical'), ('Holidays', 'Holidays'), ('Industrial', 'Industrial'), ('Interiors', 'Interiors'), ('Miscellaneous', 'Miscellaneous'), ('Objects', 'Objects'), ('Parks/Outdoor', 'Parks/Outdoor'), ('People', 'People'), ('Religion', 'Religion'), ('Science', 'Science'), ('Signs/Symbols', 'Signs/Symbols'), ('Sports/Recreation', 'Sports/Recreation'), ('Technology', 'Technology'), ('The Arts', 'The Arts'), ('Vintage', 'Vintage')], default='Parks/Outdoor', max_length=50),
        ),
    ]