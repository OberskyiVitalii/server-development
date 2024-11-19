# Generated by Django 5.1.2 on 2024-11-19 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busses', '0003_alter_busses_status'),
        ('routes', '0003_remove_routes_travel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='bus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='busses', to='busses.busses'),
        ),
    ]
