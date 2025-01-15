# Generated by Django 5.1.4 on 2025-01-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0035_alter_car_car_cover_alter_profile_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='status',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Sold', 'Sold')], default='Available', help_text='Choose part status', max_length=20),
        ),
    ]
