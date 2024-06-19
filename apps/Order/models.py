from django.db import models
from apps.products.models import Products
from django.contrib.auth.models import User

class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE);
   reference = models.CharField(max_length=100);
   status = models.BooleanField(default=False);
   total_amount = models.DecimalField(max_digits=10, decimal_places=2);
   shipping_address = models.TextField();
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

   def __str__(self):
      return self.id;

class OrderItems(models.Model):
   product = models.ForeignKey(Products, on_delete=models.CASCADE);
   order = models.ForeignKey(Order, on_delete=models.CASCADE);
   quantity = models.PositiveIntegerField();
   unit_price = models.DecimalField(max_digits=10, decimal_places=2)
   total_price = models.DecimalField(max_digits=10, decimal_places=2)
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);
