from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .cart import *
import json
from django.http import JsonResponse
from .models import CartItem

@login_required(login_url='/accounts/login')
def Add_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['pid']
        quantity = data['quantity']
        item,created=add_to_cart(request.user,product_id,quantity)
        if created :
            return JsonResponse({'status':'added'})
        else:
            return JsonResponse({'status':'exist'})

@login_required(login_url='/accounts/login')
def show_cart(request):
    cart = cart_items(request.user)
    return render(request,'cart/cart.html',{'product':cart})

@login_required
def Update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        action = data.get('action')
        update = update_to_cart(request.user,product_id,action)
        if update:
            cart = CartItem.objects.get(user=request.user,product = product_id)
            cart_price = cart.quantity*cart.product.discount_price
            return JsonResponse({'status':"added",'cart':cart.quantity,'cart_price':cart_price})
        

@login_required
def Delete_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['pid']
        delete = delete_to_cart(request.user,product_id)
        if delete:
            return JsonResponse({'status':'deleted'})
        return redirect('showcart')
    