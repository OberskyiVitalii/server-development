# Generated by Django 5.1.2 on 2024-11-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busses', '0002_remove_busses_driver_id_remove_busses_route_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busses',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]
