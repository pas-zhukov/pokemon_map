from django.db import models  # noqa F401


class Pokemon(models.Model):
    """Вид покемона"""
    title = models.TextField(max_length=20, verbose_name="Название вида")
    title_en = models.TextField(verbose_name="Название вида (англ)",
                                null=True, blank=True)
    title_jp = models.TextField(verbose_name="Название вида (яп)",
                                null=True, blank=True)
    image = models.ImageField(verbose_name="Изображение покемона",
                              null=True)
    description = models.TextField(verbose_name="Описание вида",
                                   null=True, blank=True)

    previous_evolution = models.ForeignKey('self',
                                           related_name="next_evolutions",
                                           verbose_name="Из кого покемон эволюционировал",
                                           null=True, blank=True,
                                           on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def to_dict(self):
        pokemon_stats = {
            "pokemon_id": self.id,
            "title_ru": self.title,
            "title_en": self.title_en,
            "title_jp": self.title_jp,
            "description": self.description,
            "img_url": self.image.url,
            "entities": None,

        }

        next_evolution = self.next_evolutions.first()
        if next_evolution:
            pokemon_stats["next_evolution"] = {
                "title_ru": next_evolution.title,
                "pokemon_id": next_evolution.id,
                "img_url": next_evolution.image.url
            }
        if self.previous_evolution:
            pokemon_stats["previous_evolution"] = {
                "title_ru": self.previous_evolution.title,
                "pokemon_id": self.previous_evolution.id,
                "img_url": self.previous_evolution.image.url
            }

        return pokemon_stats


class PokemonEntity(models.Model):
    """Покемон"""
    pokemon = models.ForeignKey(Pokemon,
                                related_name='entities',
                                verbose_name="вид покемона",
                                on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Дата и время появления покемона")
    disappeared_at = models.DateTimeField(verbose_name="Дата и время исчезновения покемона")

    level = models.IntegerField(verbose_name="Уровень покемона",
                                null=True, blank=True)
    health = models.IntegerField(verbose_name="Здоровье",
                                 null=True, blank=True)
    damage = models.IntegerField(verbose_name="Урон",
                                 null=True, blank=True)
    armour = models.IntegerField(verbose_name="Защита",
                                 null=True, blank=True)
    stamina = models.IntegerField(verbose_name="Выносливость",
                                  null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon.title} {self.level} уровня"
