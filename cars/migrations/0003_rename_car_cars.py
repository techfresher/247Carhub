# Generated by Django 4.2.13 on 2024-05-25 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_miles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='car',
            new_name='cars',
        ),
    ]