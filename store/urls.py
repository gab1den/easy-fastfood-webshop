from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('remove_from_basket/<int:product_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('', views.product_list, name='product_list'),
    path('busket', views.basket, name='busket'),
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
