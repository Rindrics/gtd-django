from django.urls import path
from . import views


app_name = 'item'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('capture/', views.capture, name='capture'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
