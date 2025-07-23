from django.urls import path
from .views import *

urlpatterns = [
    path('home/',Home_page,name='home_page'),
    path('product/',Product_list,name='product'),
    path('search/',search_view,name='search_page'),
    path('product_view/<int:pk>/',Product_view,name='product_view'),
]