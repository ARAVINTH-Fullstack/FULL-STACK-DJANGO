from django.shortcuts import render,redirect
from .models import *
from Reviews.models import Reviews
from Wishlist.models import Wishlish
from datetime import datetime,timedelta
from django.db.models import Q 


def Home_page(request):
    trending_product  = Product.objects.filter(trending=True)[:4]
    for_you = Product.objects.order_by('?')[:4]
    today_special = Product.objects.order_by('?')[:4]
    top_discount = Product.objects.filter(sale=True)[:7]
    lowest_price = Product.objects.filter(discount_price__lt = 60000).order_by('?')[:5]
    return render(request,'products/home.html',{'lowest_price':lowest_price,'trending_product':trending_product,'for_you':for_you,'today_special':today_special,'top_discount':top_discount})

def Product_list(request):
    category = request.GET.get("category").lower()

    if category == 'mobile':
        product = Mobile.objects.all()

    elif category == 'laptop':
        product = Laptop.objects.all()

    elif category == 'television':
        product = Television.objects.all()

    elif category == 'camera':
        product = Camera.objects.all()

    elif category == 'smartwatch':
        product = Smartwatch.objects.all()

    elif category == 'refrigerator':
        product = Refrigerator.objects.all()

    elif category == 'kitchen':
        product = Kitchenappliance.objects.all()

    elif category == 'grocery':
        product = Grocery.objects.all()

    elif category == 'fashion':
        product = Clothing.objects.all() 

    elif category == 'furniture':
        product = Furniture.objects.all()

    elif category == 'lighting':
        product = Lighting.objects.all()

    elif category == 'book':
        product = Book.objects.all()

    elif category == 'babycare':
        product = Babycare.objects.all()

    elif category == 'earbud':
        product = Earbuds.objects.all()
        
    else :
        product=Product.objects.all()

    wishlist_id = []

    if request.user.is_authenticated:
        wishlist_id = Wishlish.objects.filter(user=request.user).values_list('product_id',flat=True)

    delivery = datetime.now().date()+timedelta(days=7)
    fast = datetime.now().date()+timedelta(days=2)

    return render(request,'products/product.html',{'product':product,'wishlist_id':wishlist_id,'category':category,'delivery':delivery,'fast':fast})

def Product_view(request,pk):
    item = Product.objects.get(id=pk)
    reviews = item.reviews.all()
    user_review = None
    delivery = datetime.now().date()+timedelta(days=7)

    if request.user.is_authenticated:
        user_review = Reviews.objects.filter(product=item,user=request.user).first()
        if request.method == 'POST':
            rating = int(request.POST.get('rating'))
            comment = request.POST.get('comment')
            if user_review:
                user_review.rating=rating
                user_review.comment=comment
                user_review.save()
            else:
                Reviews.objects.create(product=item,user=request.user,rating=rating,comment=comment)
            return redirect('product_view',pk=item.id)
    review_sum = reviews.first()
    return render(request,'products/product_view.html',{'item':item,'reviews':reviews,'user_review':user_review,'delivery':delivery})

def search_view(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        if query.lower() == "trending":
            results = Product.objects.filter(trending=True)
        else:
            results = Product.objects.filter(
                Q(name__icontains=query) | 
                Q(brand__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query) |
                Q(category__category__name__icontains=query) 
        )
    wishlist_id = []

    if request.user.is_authenticated:
        wishlist_id = Wishlish.objects.filter(user=request.user).values_list('product_id',flat=True)
    
    return render(request, 'products/search.html', {'results': results, 'query': query,'wishlist_id':wishlist_id})


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)