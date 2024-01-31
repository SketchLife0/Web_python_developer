from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer} - {self.product} - {self.order_date}'