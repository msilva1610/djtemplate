from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^book/', views.book, name='book'),
    url(r'^genre/', views.genre, name='genre'),
    url(r'^tabela/', views.tabela, name='tabela'),
    url(r'^person/', views.person, name='person'),
    url(r'^group/', views.group, name='group'),
    url(r'^membership/', views.membership, name='membership'),
    url(r'^band_listing/', views.band_listing, name='band_listing'),
]
