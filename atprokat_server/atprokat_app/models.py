from django.db import models


class Car(models.Model):
    name = models.TextField(verbose_name="name", blank=True)
    text = models.TextField(verbose_name="text", blank=True)
    mileage = models.IntegerField(verbose_name="mileage", blank=True)
    doors = models.IntegerField(verbose_name="doors", blank=True)

    engines_type = models.TextField(verbose_name="engines_type", blank=True)
    max_power = models.IntegerField(verbose_name="max_power", blank=True)
    max_speed = models.IntegerField(verbose_name="max_speed", blank=True)
    acceleration_time = models.FloatField(verbose_name="acceleration_time", blank=True)
    fuel_consumption = models.FloatField(verbose_name="fuel_consumption", blank=True)
    transmission = models.TextField(verbose_name="transmission", blank=True)
    drive_unit = models.TextField(verbose_name="drive_unit", blank=True)
    seat_number = models.IntegerField(verbose_name="seat_number", blank=True)
    length = models.IntegerField(verbose_name="length", blank=True)
    trunk_volume = models.IntegerField(verbose_name="trunk_volume", blank=True)

    days1_2 = models.IntegerField(verbose_name="days1_2", blank=True)
    days3_6 = models.IntegerField(verbose_name="days3_6", blank=True)
    days7_14 = models.IntegerField(verbose_name="days7_14", blank=True)
    days15_30 = models.IntegerField(verbose_name="days15_30", blank=True)
    month1_2 = models.IntegerField(verbose_name="month1_2", blank=True)
    deposit = models.IntegerField(verbose_name="deposit", blank=True)

    image = models.ImageField(verbose_name="image", upload_to="img")

    def __str__(self):
        return self.name


class News(models.Model):
    date = models.DateField(verbose_name="date", blank=True)
    title = models.TextField(verbose_name="title", blank=True)
    text = models.TextField(verbose_name="text", blank=True)
    is_ellipsize = False

    def __str__(self):
        return "{} {}".format(self.date, self.title)
