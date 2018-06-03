from . import views
from django.urls import  path


urlpatterns = [
    path('', views.index, name="index"),
    path('tower-block', views.tower_block , name="tower_block"),
    path('2048', views.gioco2048 , name="2048"),
    path('classifica/<str:gioco>/<int:risultato>/<str:user>', views.risultato, name="risultato"),
    path('iframe-classifica/<str:gioco>',views.carica_classifica, name="carica-classifica"),
]
