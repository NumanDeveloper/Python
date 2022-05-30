from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('<int:day', views.int_day, name='day_by_number'),
    path('<str:day>', views.day_description, name='day_by_name'),
]
