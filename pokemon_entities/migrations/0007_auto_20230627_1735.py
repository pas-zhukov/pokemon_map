# Generated by Django 3.1.14 on 2023-06-27 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20230627_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemon'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolutions', to='pokemon_entities.pokemon'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.TextField(max_length=20),
        ),
    ]