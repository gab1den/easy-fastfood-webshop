from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('busket', views.busket, name='busket'),
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
