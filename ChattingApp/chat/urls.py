# chat/urls.py
from django.urls import path

from . import views

app_name = "chat"

urlpatterns = [
    path('index/', views.index, name='index'),
    path("", views.login, name="login")
]