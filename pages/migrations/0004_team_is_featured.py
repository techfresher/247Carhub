# Generated by Django 4.2.13 on 2024-05-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_team_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_featured',
            field=models.BooleanField(default=True),
        ),
    ]