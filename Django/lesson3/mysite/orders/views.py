from django.shortcuts import render
from django.utils import timezone
from .models import Order, Product

def order_list(request, days):
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)
    orders = Order.objects.filter(order_date__range=(start_date, end_date)).prefetch_related('products').order_by('-order_date')
    unique_products = set()
    for order in orders:
        unique_products.update(order.products.all())
    return render(request, 'orders/order_list.html', {'orders': orders, 'unique_products': unique_products})