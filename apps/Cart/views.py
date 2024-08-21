from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products, Cart, CartItems

""" @login_required """
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)

    cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += quantity
        if cart_item.quantity > product.quantity:
            cart_item.quantity = product.quantity
        cart_item.save()
    else:
        if quantity <= product.quantity:
            cart_item.quantity = quantity
            cart_item.save()

    """ return JsonResponse({'status': 'Product added to cart successfully.'}) """


""" @login_required """
def cart_summary(request):
    cart = Cart.objects.get(user=request.user)
    context = {
        'cart': cart,
    }

    return render(request, 'cart_summary.html', context)