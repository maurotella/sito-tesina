from . import views
from django.urls import  path


urlpatterns = [
    path('', views.index, name="index"),
    path('elimina/<str:codice>', views.cancella, name="cancella"),
]
