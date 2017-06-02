from django.db import models


class Card(models.Model):
    name = models.TextField(verbose_name="name", blank=True)
    text = models.TextField(verbose_name="text", blank=True)
    edition = models.TextField(verbose_name="edition", blank=True)
    rarity = models.TextField(verbose_name="rarity", blank=True)
    type = models.TextField(verbose_name="type", blank=True)
    manacost = models.TextField(verbose_name="manacost", blank=True)
    price = models.TextField(verbose_name="price", blank=True)
    image = models.ImageField(verbose_name="image", upload_to="img")

    def __str__(self):
        return self.name

    def sum(self, str1, str2):
        return str1 + " " + str2
