from django.urls import path
from . import views

app_name = 'calorie_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('reset/', views.reset_today, name='reset_today'),
]