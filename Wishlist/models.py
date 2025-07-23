from django.db import models
from django.contrib.auth.models import User
from Products.models import Product

class Wishlish(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='wishlists')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='wishlisted')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','product')

    def __str__(self):
        return f"{self.user.username}-{self.product.name}"
