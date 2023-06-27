from django.db import models  # noqa F401

# your models here
class Pockemon(models.Model):
    title = models.TextField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class PockemonEntity(models.Model):
    pockemon = models.ForeignKey(Pockemon, on_delete=models.CASCADE)
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
        return str(self.__dict__)
