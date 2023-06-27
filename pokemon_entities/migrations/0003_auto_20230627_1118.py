# Generated by Django 3.1.14 on 2023-06-27 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pockemon_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PockemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='pockemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
