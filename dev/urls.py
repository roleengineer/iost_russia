from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dev_en, name='dev_en'),
    path('ru/', views.dev_ru, name='dev_ru'),
]
