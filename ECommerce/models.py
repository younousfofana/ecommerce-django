from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
   complete = models.BooleanField(default=False);
   reference = models.CharField(max_length=100);
   user = models.ForeignKey(User, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

   def __str__(self):
      return self.id;

class OrderItems(models.Model):
   product = models.ForeignKey(Products, on_delete=models.CASCADE);
   order = models.ForeignKey(Order, on_delete=models.CASCADE);
   Quantity = models.IntegerField();
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class CartItems(models.Model):
   product = models.ForeignKey(Products, on_delete=models.CASCADE);
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE);
   quantity = models.IntegerField(default=0);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class Payment(models.Model):
   payment_method = models.CharField(max_length=100);
   amount = models.DecimalField(max_digits=10, decimal_places=2);
   user = models.ForeignKey(User, on_delete=models.CASCADE);
   order = models.ForeignKey(Order, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class Address(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE);
   order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True);
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
   product = models.ForeignKey(Products, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);