from django.shortcuts import render, get_object_or_404
from .models import Products, Cart, CartItems
from django.http import JsonResponse

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

    if quantity <= product.quantity:
        cart_item.quantity = quantity
        cart_item.save()

    return JsonResponse({'status': 'Product added to cart successfully.'})

def cart_summary(request):
    cartItems = []

    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        cartItems = cart.cartitems_set.all()
    else:
        session_key = request.session.session_key
        if session_key:
            cart = Cart.objects.filter(session_key=session_key).first();
            if cart:
                cartItems = cart.cartitems_set.all();
        else:
            request.session.create()
            
    total_products_in_card = len(cartItems);

    return render(request, 'cart_summary.html', {'cart_items': cartItems, 'total_products_card': total_products_in_card})