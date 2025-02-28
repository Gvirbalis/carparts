# Generated by Django 5.1.4 on 2024-12-23 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0012_remove_carmodel_brand_carbrand_alter_car_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carparts.carmodel'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(help_text='Input Brand example(Ford)', max_length=100, null=True, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='model',
            field=models.CharField(help_text='Input Model name example(Focus)', max_length=100, null=True, verbose_name='Model'),
        ),
        migrations.DeleteModel(
            name='CarBrand',
        ),
    ]
