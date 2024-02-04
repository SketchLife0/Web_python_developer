from django.db import models
from django.utils import timezone

class Order(models.Model):
    client_name = models.CharField(max_length=100, default='Anonymous')
    order_date = models.DateTimeField(default=timezone.now)

class Product(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE)

