# Generated by Django 5.1.2 on 2024-10-30 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.routes')),
            ],
        ),
    ]