from . import views
from django.urls import  path


urlpatterns = [
    path('', views.index, name="index"),
    path('aggiungi', views.aggiungi, name="aggiungi"),
    path('cerca', views.cerca, name="cerca"),
    path('elimina/<str:codice>', views.cancella, name="cancella"),
]
