from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Client, Product, Order

class ClientDetailView(DetailView):
    model = Client
    namespace = 'clients'

class ClientListView(ListView):
    model = Client
    namespace = 'clients'

class ProductDetailView(DetailView):
    model = Product
    namespace = 'products'

class ProductListView(ListView):
    model = Product
    namespace = 'products'

class OrderDetailView(DetailView):
    model = Order
    namespace = 'orders'

class OrderListView(ListView):
    model = Order
    namespace = 'orders'
    