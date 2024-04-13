from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('busket', views.busket, name='busket'),
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
]
