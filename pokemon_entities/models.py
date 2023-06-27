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
                                           related_name="previous_evolutions",
                                           verbose_name="Из кого покемон эволюционировал",
                                           null=True, blank=True,
                                           on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def to_dict(self):
        pokemon_data = {
            "pokemon_id": self.id,
            "title_ru": self.title,
            "title_en": self.title_en,
            "title_jp": self.title_jp,
            "description": self.description,
            "img_url": self.image.url,
            "entities": None,

        }
        try:
            next_evolution = Pokemon.objects.get(previous_evolution=self)
            pokemon_data["next_evolution"] = {
                "title_ru": next_evolution.title,
                "pokemon_id": next_evolution.id,
                "img_url": next_evolution.image.url
            }
        except Pokemon.DoesNotExist:
            pokemon_data["next_evolution"] = dict()
        if self.previous_evolution:
            pokemon_data["previous_evolution"] = {
                "title_ru": self.previous_evolution.title,
                "pokemon_id": self.previous_evolution.id,
                "img_url": self.previous_evolution.image.url
            }

        return pokemon_data


class PokemonEntity(models.Model):
    """Покемон"""
    pokemon = models.ForeignKey(Pokemon,
                                verbose_name="вид покемона",
                                on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Дата и время появления покемона")
    disappeared_at = models.DateTimeField(verbose_name="Дата и время исчезновения покемона")

    level = models.IntegerField(default=1,
                                verbose_name="Уровень покемона",
                                null=True, blank=True)
    health = models.IntegerField(default=100,
                                 verbose_name="Здоровье",
                                 null=True, blank=True)
    damage = models.IntegerField(default=18,
                                 verbose_name="Урон",
                                 null=True, blank=True)
    armour = models.IntegerField(default=0,
                                 verbose_name="Защита",
                                 null=True, blank=True)
    stamina = models.IntegerField(default=20,
                                  verbose_name="Выносливость",
                                  null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon.title} {self.level} уровня"
