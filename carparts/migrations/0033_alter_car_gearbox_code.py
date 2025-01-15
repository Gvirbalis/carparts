# Generated by Django 5.1.4 on 2025-01-09 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0032_car_engine_code_car_gearbox_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='gearbox_code',
            field=models.CharField(blank=True, help_text='Input Gearbox code', max_length=100, verbose_name='Gearbox Code'),
        ),
    ]
