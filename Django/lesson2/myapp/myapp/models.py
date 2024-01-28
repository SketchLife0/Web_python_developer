from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    addition_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"