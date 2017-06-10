from django.conf.urls import url
from xstock import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^buy2/$', views.buy, name='buy2'),
    url(r'^history/$', views.history, name='history'),
    url(r'^summary/$', views.summary, name='summary'),

    url(r'^about/$', views.about, name='about'),
]