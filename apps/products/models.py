from django.db import models

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