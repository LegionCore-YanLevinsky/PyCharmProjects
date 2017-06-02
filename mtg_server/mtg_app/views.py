from django.shortcuts import render, HttpResponseRedirect, Http404, get_object_or_404
from django.contrib import auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from mtg_app.forms import MyRegistrationForm
from mtg_app.models import Card


def index(request):
    title = "Home"
    page = "index"
    return render(request, 'index.html', {
        'title': title,
        'page': page})


def about(request):
    title = "About"
    page = "about"
    return render(request, 'about.html', {
        'title': title,
        'page': page})


def card_list(request):
    title = "Card list"
    page = "cards"
    card_list = Card.objects.all()

    paginator = Paginator(card_list, 5)
    page_numb = request.GET.get('page')

    try:
        cards = paginator.page(page_numb)
    except PageNotAnInteger:
        cards = paginator.page(1)
    except EmptyPage:
        cards = paginator.page(paginator.num_pages)

    return render(request, 'card_list.html', {
        'title': title,
        'page': page,
        'cards': cards})


class CardListView(ListView):
    model = Card
    template_name = 'card_list.html'
    paginate_by = 5


def item(request, num='0'):
    title = "Card"
    page = "cards"
    card = get_object_or_404(Card, id=num)
    return render(request, "item.html", {
        'title': title,
        'page': page,
        'card': card})


class CardDetailView(DetailView):
    title = "Card"
    page = "cards"

    model = Card
    template_name = 'item.html'


def rules(request):
    title = "Rules"
    page = "rules"
    return render(request, 'rules.html', {
        'title': title,
        'page': page})


def login(request):
    if request.method != 'POST':
        raise Http404

    title = "Log in"
    page = "rules"

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)

    if user:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        page = "index"
        return render(request, 'index.html', {
            'title': title, 'page': page,
            'username': username,
            'errors': True})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def registration(request):
    title = "Registration"
    page = "registration"

    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'registration.html', {
            'title': title,
            'page': page,
            'form': form})
    return render(request, 'registration.html', {
        'title': title,
        'page': page,
        'form': MyRegistrationForm()})
