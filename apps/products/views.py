from urllib import request
from django.shortcuts import render
from apps.products.models import Products

def index(request):
    products_list = Products.objects
    context = {
        "products_list" : products_list
    }
    return render(request,"products/index.html", context)