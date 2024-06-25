from urllib import request
from django.shortcuts import render
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