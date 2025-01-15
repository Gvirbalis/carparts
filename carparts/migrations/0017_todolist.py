# Generated by Django 5.1.4 on 2024-12-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparts', '0016_alter_part_part_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_progress', models.CharField(blank=True, choices=[('new', 'New'), ('working', 'Working'), ('stuck', 'Stuck'), ('pause', 'Pause'), ('almost done', 'Almost Done'), ('done', 'Done')], default='new', help_text='Progresive', max_length=100, null=True)),
                ('name', models.CharField(help_text='Input name progress', max_length=100, null=True, verbose_name='Name')),
                ('comment', models.CharField(help_text='Input comment', max_length=100, null=True, verbose_name='Comment')),
            ],
        ),
    ]
