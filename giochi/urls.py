from . import views
from django.urls import  path


urlpatterns = [
    path('', views.index, name="index"),
    path('stack', views.stack , name="stack"),
    path('2048', views.gioco2048 , name="2048"),
    path('classifica/<str:gioco>/<int:risultato>/<str:user>', views.risultato, name="risultato"),
    path('iframe-classifica/<str:gioco>',views.carica_classifica, name="carica-classifica"),
    path('snake',views.snake, name="snake"),
    path('flappy_bird',views.flappy_bird, name="flappy_bird"),
    path('super_hexagon',views.super_hexagon, name="super_hexagon"),
]
