# Generated by Django 4.2.4 on 2023-08-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_videogame_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='description',
            field=models.TextField(default=0, max_length=500),
            preserve_default=False,
        )
    ]