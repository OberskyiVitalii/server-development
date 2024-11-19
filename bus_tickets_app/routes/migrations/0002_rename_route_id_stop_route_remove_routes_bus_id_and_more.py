# Generated by Django 5.1.2 on 2024-11-19 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busses', '0002_remove_busses_driver_id_remove_busses_route_id_and_more'),
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stop',
            old_name='route_id',
            new_name='route',
        ),
        migrations.RemoveField(
            model_name='routes',
            name='bus_id',
        ),
        migrations.AddField(
            model_name='routes',
            name='bus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='busses.busses'),
        ),
    ]
