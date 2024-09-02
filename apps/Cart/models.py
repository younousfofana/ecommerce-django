from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Products

class Cart(models.Model):
   user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE);
   session_key = models.CharField(max_length=40, null=True, blank=True);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

   def __str__(self):
      return f"Panier {self.id}"

class CartItems(models.Model):
   product = models.ForeignKey(Products, on_delete=models.CASCADE);
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE);
   quantity = models.IntegerField(default=0);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

   def __str__(self):
      return f"{self.product.name} : {self.quantity}";