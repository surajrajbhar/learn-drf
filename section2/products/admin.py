from django.contrib import admin
from .models import Manufacturers, Products

# Register your models here.

admin.site.register(Manufacturers)
admin.site.register(Products)