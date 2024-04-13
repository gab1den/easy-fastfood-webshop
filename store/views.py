from django.shortcuts import render, redirect

from .models import Product, Basket

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def add_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    basket, created = Basket.objects.get_or_create(product=product)
    basket.quantity += 1
    basket.save()
    return redirect('product_list')

def busket(request):
    basket = Basket.objects.all()
    return render(request, 'store/basket.html', {'basket': basket})
