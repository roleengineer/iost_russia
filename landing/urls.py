from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_en, name='index_en'),
    path('ru/', views.index_ru, name='index_ru'),
]
