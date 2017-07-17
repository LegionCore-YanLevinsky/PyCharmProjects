from django.shortcuts import render, get_object_or_404
from atprokat_app.models import Car, News
import datetime


def index(request):
    all_news = News.objects.all()
    last_news = [all_news.last(), all_news[len(all_news) - 2]]
    for news in last_news:
        if len(news.text) > 128:
            news.text = (news.text[:128] + '...')
            news.is_ellipsize = True

    context = {
        'title': 'Автотур | Прокат автомобилей в Сочи',
        'page': 'index',
        'cars': Car.objects.all(),
        'news': last_news}
    context.update(get_time_frames())
    return render(request, 'index.html', context)


def autopark(request):
    context = {
        'title': 'Автопрокат',
        'page': 'autopark',
        'cars': Car.objects.all()}
    context.update(get_time_frames())
    return render(request, 'autopark.html', context)


def rates(request):
    context = {
        'title': 'Тарифы',
        'page': 'rates'}
    context.update(get_time_frames())
    return render(request, 'rates.html', context)


def services(request):
    context = {
        'title': 'Услуги',
        'page': 'services'}
    context.update(get_time_frames())
    return render(request, 'services.html', context)


def question_answer(request):
    context = {
        'title': 'Вопрос-ответ',
        'page': 'question_answer'}
    context.update(get_time_frames())
    return render(request, 'question_answer.html', context)


def routes(request):
    context = {
        'title': 'Маршруты',
        'page': 'routes'}
    context.update(get_time_frames())
    return render(request, 'routes.html', context)


def stocks(request):
    context = {
        'title': 'Акции',
        'page': 'stocks'}
    context.update(get_time_frames())
    return render(request, 'stocks.html', context)


def news(request):
    context = {
        'title': 'Новости',
        'page': 'news'}
    context.update(get_time_frames())
    return render(request, 'news.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
        'page': 'contacts'}
    context.update(get_time_frames())
    return render(request, 'contacts.html', context)


def car_item(request, num='0'):
    car = get_object_or_404(Car, id=num)
    context = {
        'title': car.name,
        'page': "cars",
        'car': car}
    context.update(
        get_time_frames())
    return render(request, "item.html", context)


def get_time_frames():
    date_from = datetime.datetime.today()
    date_to = date_from + datetime.timedelta(days=5)
    date_from = date_from.strftime('%Y-%m-%d')
    date_to = date_to.strftime('%Y-%m-%d')
    return {'date_from': date_from, 'date_to': date_to}
