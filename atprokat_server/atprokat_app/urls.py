from django.conf.urls import url
from atprokat_app.views import index, autopark, rates, services, question_answer, routes, stocks, news, contacts, car_item

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^autopark/$', autopark, name='autopark'),
    url(r'^rates/$', rates, name='rates'),
    url(r'^services/$', services, name='services'),
    url(r'^question_answer/$', question_answer, name='question_answer'),
    url(r'^routes/$', routes, name='routes'),
    url(r'^stocks/$', stocks, name='stocks'),
    url(r'^news/$', news, name='news'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^autopark/(?P<num>\d+)/$', car_item, name='item'),
]
