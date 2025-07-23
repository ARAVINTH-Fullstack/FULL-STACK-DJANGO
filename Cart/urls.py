from django.urls import path
from .views import *

urlpatterns = [
    path('addcart',Add_cart,name='addcart'),
    path('updatecart',Update_cart,name='updatecart'),
    path('deletecart',Delete_cart,name='deletecart'),
    path('showcart',show_cart,name='showcart'),
]
