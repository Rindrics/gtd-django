from django.urls import path
from . import views


app_name = 'item'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inbox/', views.capture, name='inbox'),
    path('inbox/update/<int:item_id>/', views.update_item, name='update_item'),
    path('inbox/delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
