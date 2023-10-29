from django.contrib import admin
from . models import Products,Order,User
# Register your models here.
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(User)