from django.db import models
from django.contrib.auth.models import User
from Products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user','product')

    def total_price(self):
        return self.product.discount_price*self.quantity
    
