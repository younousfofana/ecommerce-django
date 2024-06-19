from django.db import models
from django.contrib.auth.models import User

""" class User(AbstractUser):
   pass; """

class Category(models.Model):
    name = models.CharField(max_length=255);
    description = models.TextField();
    created_at = models.DateTimeField(auto_now=True);
    updated_at = models.DateTimeField(null=True, blank=True);

    def __str__(self):
     return self.name;

class Products(models.Model):
   name = models.CharField(max_length=255);
   description = models.TextField();
   price = models.DecimalField(max_digits=10, decimal_places=2);
   stock = models.IntegerField();
   image = models.CharField(max_length=255);
   category_id = models.ForeignKey(Category, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

   def __str__(self):
     return self.name;

class Order(models.Model):
   complete = models.BooleanField(default=False);
   reference = models.CharField(max_length=100);
   user_id = models.ForeignKey(User, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

   def __str__(self):
      return self.id;

class OrderItems(models.Model):
   product_id = models.ForeignKey(Products, on_delete=models.CASCADE);
   order_id = models.ForeignKey(Order, on_delete=models.CASCADE);
   Quantity = models.IntegerField();
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class Cart(models.Model):
   user_id = models.ForeignKey(User, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class CartItems(models.Model):
   product_id = models.ForeignKey(Products, on_delete=models.CASCADE);
   cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE);
   quantity = models.IntegerField(default=0);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class Payment(models.Model):
   payment_method = models.CharField(max_length=100);
   amount = models.DecimalField(max_digits=10, decimal_places=2);
   user_id = models.ForeignKey(User, on_delete=models.CASCADE);
   order_id = models.ForeignKey(Order, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class Address(models.Model):
   user_id = models.ForeignKey(User, on_delete=models.CASCADE);
   order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True);
   address_line_1 = models.CharField(max_length=255);
   address_line_2 = models.CharField(max_length=255, null=True, blank=True);
   city = models.CharField(max_length=100);
   state = models.CharField(max_length=100);
   postal_code = models.CharField(max_length=20);
   country = models.CharField(max_length=100);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class ProductImage(models.Model):
   url = models.CharField(max_length=255);
   product_id = models.ForeignKey(Products, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);