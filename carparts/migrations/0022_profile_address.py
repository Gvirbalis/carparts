# Generated by Django 5.1.4 on 2025-01-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0021_profile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(help_text='Input address example(Verkiu g. 2)', max_length=100, null=True, verbose_name='Address'),
        ),
    ]
