from django.urls import path
from . import views


app_name = 'item'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('capture/', views.capture, name='capture'),
]
