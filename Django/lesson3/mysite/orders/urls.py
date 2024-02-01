from django.urls import path
from . import views

urlpatterns = [
    path('7days/', views.order_list, {'days': 7}, name='order_list_7days'),
    path('30days/', views.order_list, {'days': 30}, name='order_list_30days'),
    path('365days/', views.order_list, {'days': 365}, name='order_list_365days'),
]