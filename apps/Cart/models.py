from django.db import models
from django.contrib.auth.models import User
from apps.products import Products

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