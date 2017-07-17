from django.contrib import admin
from  books_app.models import Book, Author, Genre, CycleOfStories

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(CycleOfStories)
