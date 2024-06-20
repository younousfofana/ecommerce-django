from django.db import models
from django.contrib.auth.models import User

from apps.Order.models import Order

class Payment(models.Model):
   payment_method = models.CharField(max_length=100);
   amount = models.DecimalField(max_digits=10, decimal_places=2);
   user = models.ForeignKey(User, on_delete=models.CASCADE);
   order = models.ForeignKey(Order, on_delete=models.CASCADE);
   created_at = models.DateTimeField(auto_now=True);
   updated_at = models.DateTimeField(null=True, blank=True);
