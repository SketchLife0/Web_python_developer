from django.shortcuts import render
from django.http import HttpResponse
import logging

# Получаем экземпляр логгера
logger = logging.getLogger('myapp')

def home(request):
    logger.info(f"Visited Home. IP: {request.META.get('REMOTE_ADDR')}")
    return render(request, 'myapp/home.html')

def about_me(request):
    logger.info(f"Visited About me. IP: {request.META.get('REMOTE_ADDR')}")
    return render(request, 'myapp/about_me.html')