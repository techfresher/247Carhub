# Generated by Django 4.2.13 on 2024-05-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_condition_alter_car_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='minage',
            field=models.TextField(max_length=150),
        ),
    ]