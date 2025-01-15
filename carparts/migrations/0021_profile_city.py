# Generated by Django 5.1.4 on 2025-01-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0020_part_owner_alter_profile_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(help_text='Input city name example(Vilnius)', max_length=100, null=True, verbose_name='City'),
        ),
    ]
