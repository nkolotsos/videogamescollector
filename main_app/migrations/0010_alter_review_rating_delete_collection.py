# Generated by Django 4.2.4 on 2023-08-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_videogame_collections_collection_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 'R1'), (2, 'R2'), (3, 'R3'), (4, 'R4'), (5, 'R5')]),
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
    ]
