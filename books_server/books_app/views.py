from django.shortcuts import render, Http404, HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.contrib import auth
from books_app.models import Book, Genre, Author
from books_app.forms import MyRegistrationForm


def index(request):
    context = {
        'title': 'books.ru',
        'genres': get_list_or_404(Genre),
        'authors': get_list_or_404(Author)
    }
    return render(request, 'index.html', context)


def books(request):
    context = {
        'title': 'books.ru',
        'books': get_list_or_404(Book),
        'genres': get_list_or_404(Genre),
        'authors': get_list_or_404(Author)
    }
    return render(request, 'books.html', context)


def books_by_genre(request, genre):
    context = {
        'title': 'books.ru',
        'books': get_list_or_404(Book, genre=genre),
        'genres': get_list_or_404(Genre),
        'authors': get_list_or_404(Author)
    }
    return render(request, 'books.html', context)


def books_by_author(request, author):
    context = {
        'title': 'books.ru',
        'books': get_list_or_404(Book, author=author),
        'genres': get_list_or_404(Genre),
        'authors': get_list_or_404(Author)
    }
    return render(request, 'books.html', context)


def book(request, num='0'):
    context = {
        'title': 'books.ru',
        'book': get_object_or_404(Book, id=num),
        'genres': get_list_or_404(Genre),
        'authors': get_list_or_404(Author)
    }
    return render(request, "book.html", context)


def login(request):
    if request.method != 'POST':
        raise Http404

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)

    if user:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        context = {
            'title': 'Log in',
            'genres': get_list_or_404(Genre),
            'authors': get_list_or_404(Author),
            'login': username,
            'errors': True}
        return render(request, 'index.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def registration(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'registration.html', {
            'title': "books.ru",
            'genres': get_list_or_404(Genre),
            'authors': get_list_or_404(Author),
            'form': form})
    return render(request, 'registration.html', {
        'title': "books.ru",
        'genres': get_list_or_404(Genre),
        'authors': get_list_or_404(Author),
        'form': MyRegistrationForm()})
