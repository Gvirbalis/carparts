# Generated by Django 5.1.4 on 2025-01-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0036_part_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('Not verified', 'Not verified'), ('Verified', 'Verified')], default='Not verified', help_text='Choose profile status', max_length=20),
        ),
    ]
