# Generated by Django 4.2.4 on 2023-08-27 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_videogame_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogame',
            name='rating',
        ),
    ]
