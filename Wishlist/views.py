from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wishlish
from Products.models import Product
from django.http import JsonResponse

def Toggle_wishlist(request,productId):
    if request.method == 'POST':
        product_id = productId
        product = Product.objects.get(id=product_id)
        wishlist_item,created = Wishlish.objects.get_or_create(user=request.user,product=product)

        if not created:
            wishlist_item.delete()
            return JsonResponse({'status':'removed'})
        
        return JsonResponse({'status':'added'})

@login_required(login_url='/accounts/login')
def Wishlist_view(request):
    wishlist = Wishlish.objects.filter(user=request.user).select_related('product')
    return render(request,'wishlist.html',{'wishlist':wishlist})
