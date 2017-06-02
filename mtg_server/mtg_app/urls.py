from django.conf.urls import url
from mtg_app.views import index, about, CardListView, rules, registration, login, logout, CardDetailView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^cards/$', CardListView.as_view(), name='cards'),
    url(r'^cards/(?P<pk>\d+)/$', CardDetailView.as_view(), name='item'),
    url(r'^rules/$', rules, name='rules'),
    url(r'^registration/$', registration, name='registration'),
]
