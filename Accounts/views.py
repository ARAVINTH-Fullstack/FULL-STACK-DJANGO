from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import Profile,Vendor

def Signup(request):
    form = SignupForm()
    if request.method == 'POST':
        user = SignupForm(request.POST)
        if user.is_valid:
            user.save()
            return redirect('home_page')
        else:
            return redirect('signup_page')
    return render(request,'signup.html',{'form':form})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user.is_authenticated:
            login(request,user)
            return redirect('home_page')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('home_page')

def Profile_view(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
    return render(request,'profile.html',{'profile':profile})

def Add_vendor(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            shop_name = request.POST['shop_name']
            vendor_number = request.POST['vendor_number']
            vendor_address = request.POST['vendor_address']
            vendor = Vendor(user=user,shop_name=shop_name,vendor_number=vendor_number,vendor_address=vendor_address)
            vendor.save()
            return redirect('home_page')
    return render(request,'vendor.html')

def Add_profile(request):
    if request.method == 'POST':
            profile = request.POST['profile']
            mobile = request.POST['mobile']
            address = request.POST['address']
            city = request.POST['city']
            country = request.POST['country']
            pin_code = request.POST['pin_code']
            form = Profile(user=request.user,profile=profile,mobile=mobile,address=address,city=city,country=country,pin_code=pin_code)
            form.save()
            return redirect('profile_page')
    return render(request,'add_profile.html')
