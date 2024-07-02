from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="productsList"),
    path('products/<int:product_id>', views.productDetail, name="productDetail"),
    path('category/<int:category_id>', views.categoryDetail, name="categoryDetail"),
]