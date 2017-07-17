from django.conf.urls import url
from books_app.views import index, books, books_by_genre, books_by_author, book, login, logout, registration

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^books/$', books, name='books'),
    url(r'^books/genres/(?P<genre>\d+)/$', books_by_genre, name='books_by_genre'),
    url(r'^books/authors/(?P<author>\d+)/$', books_by_author, name='books_by_author'),
    url(r'^books/(?P<num>\d+)/$', book, name='book'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^registration/$', registration, name='registration'),
]
