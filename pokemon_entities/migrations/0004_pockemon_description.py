# Generated by Django 3.1.14 on 2023-06-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20230627_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='pockemon',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]