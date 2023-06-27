from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField(max_length=20)
    title_en = models.TextField(blank=True)
    title_jp = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)

    previous_evolution = models.ForeignKey('self', related_name="previous_evolutions", null=True, blank=True, on_delete=models.SET_NULL)

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
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)

    level = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
    damage = models.IntegerField(default=18)
    armour = models.IntegerField(default=0)
    stamina = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.pokemon.title} {self.level} уровня"
