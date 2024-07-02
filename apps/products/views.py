from urllib import request
from django.shortcuts import render, get_object_or_404
from apps.products.models import Products, Category

def index(request):
    """ products_list = Products.objects
    context = {
        "products_list" : products_list
    } """
    categories = Category.objects.all();
    products = Products.objects.all();
    context = {
        "categories" : categories,
        "products" : products
    }
    return render(request,"products/index.html", context)

def productDetail(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    context = {
        "product" : product
    }
    return render(request, "products/product_detail.html", context)

def categoryDetail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context= {
        category: category
    }
    return render(request, "products/category_detail.html", context);