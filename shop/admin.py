from django.contrib import admin

# Register your models here.
from .models import Products
from .models import Contact



admin.site.register(Contact)

admin.site.register(Products)