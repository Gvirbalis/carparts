# Generated by Django 5.1.4 on 2024-12-23 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0011_alter_car_car_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='brand',
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(help_text='Input Brand example(Ford)', max_length=100, verbose_name='Brand')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carparts.carmodel')),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carparts.carbrand'),
        ),
    ]
