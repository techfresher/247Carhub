# Generated by Django 4.2.13 on 2024-05-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_car_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='black', max_length=50),
            preserve_default=False,
        ),
    ]
