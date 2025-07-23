from django.urls import path
from .views import Toggle_wishlist,Wishlist_view

urlpatterns = [
    path('toggle/<int:productId>/',Toggle_wishlist,name='toggle_wishlist'),
    path('my/',Wishlist_view,name='wishlist_view'),
]
