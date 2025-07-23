from django.urls import path 
from .views import *

urlpatterns = [
    path('signup',Signup,name='signup_page'),
    path('login',Login,name='login_page') ,
    path('logout',logout_view,name='logout_page') ,
    path('profile',Profile_view,name='profile_page') ,
    path('vendor',Add_vendor,name='vendor'),
    path('add_profile',Add_profile,name='add_profile'),

]
