# Generated by Django 5.1.4 on 2025-01-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0026_alter_car_body_type_alter_part_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='side',
            field=models.CharField(blank=True, choices=[('left', 'Left'), ('right', 'Right'), ('rear-left', 'Rear-Left'), ('rear-right', 'Rear-Right')], help_text='Choose part side', max_length=20),
        ),
    ]
