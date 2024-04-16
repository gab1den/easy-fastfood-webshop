from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Basket


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

@login_required
def add_to_basket(request, product_id):
    product = Product.objects.get(pk=product_id)

    basket_item, created = Basket.objects.get_or_create(user=request.user, product=product)

    # Если товар уже есть в корзине, увеличиваем количество на 1
    if not created:
        basket_item.quantity += 1
        basket_item.save()
    return redirect('product_list')

@login_required
def remove_from_basket(request, product_id):
    basket_items = Basket.objects.filter(user=request.user, product=product_id)
    basket_items.delete()
    return redirect('busket')


@login_required
def basket(request):
    user = request.user
    if user.is_authenticated:
        basket_items = Basket.objects.filter(user=user)
        return render(request, 'store/basket.html', {'basket_items': basket_items})
    else:
        return redirect('register')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('product_list')
