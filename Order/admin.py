from django.contrib import admin
from .models import Shipping_address,Order,Orderitem

admin.site.register(Shipping_address)
admin.site.register(Order)
admin.site.register(Orderitem)
