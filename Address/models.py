from django.db import models
from django.contrib.auth.models import User
from apps.Order import Order

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

