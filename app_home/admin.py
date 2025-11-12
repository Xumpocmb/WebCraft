from django.contrib import admin

# Register your models here.
from .models import Service, Price

admin.site.register(Service)
admin.site.register(Price)
