from django.db import models
from django.contrib.auth.models import User

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
   quantity = models.IntegerField(default=0);
   image = models.ImageField(blank=True);
   category = models.ForeignKey(Category, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

   def __str__(self):
     return self.name;

class ProductImage(models.Model):
   url = models.URLField();
   product = models.ForeignKey(Products, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

class Comment(models.Model):
   product = models.ForeignKey(Products, related_name='comments', on_delete=models.CASCADE);
   user = models.ForeignKey(User, on_delete=models.CASCADE);
   content = models.TextField();
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);

   def __str__(self):
      return f"Commente par {self.user.username} on {self.product.name}"