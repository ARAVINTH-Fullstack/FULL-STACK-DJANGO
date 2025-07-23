from django.urls import path
from .views import *

urlpatterns = [
    path('buy/<int:product_id>/',Buy_now,name='buy'),
    path('track/',Track_order,name='track_order'),
    path('cancel/<int:order_id>/',Cancel_order,name='cancel_order'),
]
