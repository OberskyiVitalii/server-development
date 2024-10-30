# Generated by Django 5.1.2 on 2024-10-30 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=4)),
                ('number_plate', models.CharField(max_length=10)),
                ('driver_id', models.CharField(max_length=50)),
                ('number_of_seats', models.IntegerField()),
                ('route_id', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]