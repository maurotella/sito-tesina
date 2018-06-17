from . import views
from django.urls import  path


urlpatterns = [
    path('', views.index, name="index"),
    path('cancella/<str:codice>', views.cancella, name="cancella"),
]
