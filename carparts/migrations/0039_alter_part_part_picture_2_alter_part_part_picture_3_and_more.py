# Generated by Django 5.1.4 on 2025-01-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0038_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_picture_2',
            field=models.ImageField(default='part_pics/no-image.jpg', null=True, upload_to='covers', verbose_name='Cover2'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_picture_3',
            field=models.ImageField(default='part_pics/no-image.jpg', null=True, upload_to='covers', verbose_name='Cover3'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_picture_4',
            field=models.ImageField(default='part_pics/no-image.jpg', null=True, upload_to='covers', verbose_name='Cover4'),
        ),
    ]
