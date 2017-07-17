from django.db import models
from django.core.validators import MaxValueValidator
import datetime


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        'name', max_length=32, blank=True)
    second_name = models.CharField(
        'second name', max_length=32, blank=True)
    last_name = models.CharField(
        'last name', max_length=32, blank=True)

    def __str__(self):
        return "{}. {}. {}".format(self.first_name[0], self.second_name[0], self.last_name)


class Genre(models.Model):
    name = models.TextField('name')

    def __str__(self):
        return self.name


class CycleOfStories(models.Model):
    title = models.CharField(
        'title', max_length=126, blank=True)
    author = models.ForeignKey(
        Author, models.PROTECT, verbose_name='author', blank=True)

    def __str__(self):
        return "{}, {}".format(self.title, self.author)


class Book(models.Model):
    current_year = datetime.datetime.now().year

    title = models.CharField(
        'title', max_length=126, blank=True)
    author = models.ForeignKey(
        Author, models.PROTECT, verbose_name='author', blank=True)
    cycle = models.ForeignKey(
        CycleOfStories, models.PROTECT, verbose_name='cycle of stories', blank=True)
    genre = models.ManyToManyField(
        Genre, verbose_name='genre'
    )
    year_of_publication = models.PositiveIntegerField(
        'year of publication', default=current_year, validators=[MaxValueValidator(current_year)], blank=True)
    description = models.TextField(
        'description', blank=True)

    book_path = 'test'

    image = models.ImageField(
        'image', upload_to=book_path, blank=True)
    file_txt = models.FileField(
        '*.txt', upload_to=book_path, blank=True)
    file_fb2 = models.FileField(
        '*.fb2', upload_to=book_path, blank=True)

    def __str__(self):
        return "{}, {}".format(self.title, self.author)
