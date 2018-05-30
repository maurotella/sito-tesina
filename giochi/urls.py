from . import views
from django.urls import  path


urlpatterns = [
    path('', views.index, name="index"),
    path('tower-block', views.tower_block , name="tower_block"),
]
