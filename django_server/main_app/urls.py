from django.conf.urls import url
from  main_app.views import main, about, zak, login

urlpatterns = [
    url(r'^$', main, name="main"),
    url(r'^about/$', about, name="about"),
    url(r'^zak/$', zak, name="zak"),
    url(r'^login$', login, name="login"),
]
