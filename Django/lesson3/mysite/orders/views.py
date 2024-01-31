from django.shortcuts import render
from django.utils import timezone
from .models import Order

def order_list(request, days):
    if days == 'week':
        start_date = timezone.now() - timezone.timedelta(days=7)
    elif days == 'month':
        start_date = timezone.now() - timezone.timedelta(days=30)
    elif days == 'year':
        start_date = timezone.now() - timezone.timedelta(days=365)
    else:
        start_date = None

    if start_date:
        orders = Order.objects.filter(order_date__gte=start_date).order_by('-order_date')
        unique_orders = {order.product.name: order for order in orders}.values()
    else:
        unique_orders = []

    return render(request, 'orders/order_list.html', {'orders': unique_orders})

