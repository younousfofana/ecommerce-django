from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products, Cart, CartItems
from django.http import JsonResponse

""" @login_required """
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    print('quantite envoye depuis le formulaire', quantity);

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)

    cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)

    # Mettre à jour la quantité avec la nouvelle valeur sans ajouter à l'existante
    if quantity <= product.quantity:
        cart_item.quantity = quantity
        cart_item.save()

    return JsonResponse({'status': 'Product added to cart successfully.'})


""" @login_required """
def cart_summary(request):
    # Récupération du panier de l'utilisateur connecté ou du panier de session
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            cart = None
        else:
            cart = Cart.objects.get(session_key=session_key)
            print('le panier de session', cart);
        cartItems = cart.cartitems_set.all() if cart else []

    return render(request, 'cart_summary.html', {'cart_items' : cartItems})