from django.db import models


class Card(models.Model):
    manacost = models.TextField(verbose_name="manacost", blank=True)
    img = models.TextField(verbose_name="path", blank=True)
    name = models.TextField(verbose_name="name", blank=True)
    text = models.TextField(verbose_name="text", blank=True)
    price = models.TextField(verbose_name="price", blank=True)
    image = models.ImageField(verbose_name="image", upload_to="card_images")

    def __str__(self):
        return self.name


class Booster(models.Model):
    name = models.TextField(verbose_name="name", blank=True)
    color = models.TextField(verbose_name="color", blank=True)
    price = models.TextField(verbose_name="price", blank=True)
    cards = models.ForeignKey(Card, verbose_name="card")

    def __str__(self):
        return self.name
