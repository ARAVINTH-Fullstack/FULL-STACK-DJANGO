from django.db import models
from Products.models import Product
from django.contrib.auth.models import User
from django.db.models import Avg,Count

class Reviews(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['product','user']

    def __str__(self):
        return f"{self.product.name}-{self.user.username}"
    
    @property
    def total_reviews(self):
        return Reviews.objects.filter(product=self.product).count
    
    @property
    def average_rating(self):
        avg = Reviews.objects.filter(product=self.product).aaggregate(avg_rating=Avg('rating'))['avg_rating']
        return round(avg or 0,1)
