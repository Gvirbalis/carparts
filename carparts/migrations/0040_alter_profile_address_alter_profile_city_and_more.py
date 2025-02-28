# Generated by Django 5.1.4 on 2025-01-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0039_alter_part_part_picture_2_alter_part_part_picture_3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, help_text='Input address example(Verkiu g. 2)', max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, help_text='Input city name example(Vilnius)', max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Input phone number example(+37062222222)', max_length=100, null=True, verbose_name='Phone number'),
        ),
    ]
