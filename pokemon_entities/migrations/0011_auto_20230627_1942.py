# Generated by Django 3.1.14 on 2023-06-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20230627_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание вида'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изображение покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Название вида (англ)'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.TextField(blank=True, null=True, verbose_name='Название вида (яп)'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(verbose_name='Дата и время появления покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='armour',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='damage',
            field=models.IntegerField(blank=True, default=18, null=True, verbose_name='Урон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(verbose_name='Дата и время исчезновения покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, default=100, null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Уровень покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, default=20, null=True, verbose_name='Выносливость'),
        ),
    ]
