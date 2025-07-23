from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
from django.utils import timezone

class Shipping_address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='shipping_address')
    full_name = models.CharField(max_length=100)
    shipping_mobile = models.CharField(max_length=10)
    shipping_address = models.TextField()
    shipping_city = models.CharField(max_length=200)
    shipping_pin = models.CharField(max_length=10)
    shipping_country = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name},{self.shipping_city}"
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Shipping_address,on_delete=models.CASCADE)
    product_total = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField()
    is_canceled = models.BooleanField(default=False)
    order_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id}"
    
    def get_order(self):
        return Order.objects.filter(user=self.user).count()
    
    @property
    def order_total_price(self):
        return sum(item.product.discount_price for item in self.items.all())

category_choice = [
    ('pen','pending'),
    ('pro','processing'),
    ('shp','shipped'),
    ('del','delivered'),
    ]

class Orderitem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.PositiveIntegerField(default=1)
    order_price = models.PositiveIntegerField()
    # status = models.CharField(max_length=3,choices=category_choice,default='pen')

    def __str__(self):
        return f"{self.quantity} * {self.product.name}"