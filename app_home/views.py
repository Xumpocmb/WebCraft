from django.shortcuts import render
from .models import Service, Price

# Create your views here.

def home(request):
    services = Service.objects.all()
    prices = Price.objects.all()
    context = {'services': services, 'prices': prices}
    return render(request, 'index.html', context)
