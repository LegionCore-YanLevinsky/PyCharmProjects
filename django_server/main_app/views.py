from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404
from main_app.models import Card


def main(request):
    page = 'main'
    title = 'My title, bitch'
    return render(request, "index.html", {'page': page, 'title': title})


def about(request):
    page = 'about'
    title = 'about me title'
    cards = Card.objects.all()
    return render(request, "about.html", {'page': page, 'title': title, 'cards': cards})


def zak(request):
    page = 'zak'
    return render(request, "zak_base.html", {'page': page})


def login(request):
    page = 'main'
    title = 'My title, bitch'

    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "index.html", {'page': page, 'title': title, 'username': username, 'errors': True})
    raise Http404
