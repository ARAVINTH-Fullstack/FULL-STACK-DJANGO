from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Order,Orderitem,Shipping_address
from Products.models import Product
from .forms import ShippingForm
from datetime import datetime,timedelta
import json
from django.core.serializers.json import DjangoJSONEncoder

@login_required
def Buy_now(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid:
            shipping=form.save(commit=False)
            shipping.user = request.user
            shipping.save()

            total = product.discount_price
            order = Order.objects.create(user=request.user,shipping_address=shipping,total_price=total)
            Orderitem.objects.create(order=order,product=product,order_price=total)

            order_id=order.id
            return redirect('track_order')
    shipping_form=ShippingForm()

    delivery = datetime.now().date()+timedelta(days=7)
        
    return render(request,'order/buy_now.html',{'product':product,'form':shipping_form,'delivery':delivery})


@login_required
def Track_order(request): 
    orders = Orderitem.objects.filter(order__user=request.user)
    delivery = datetime.now().date()+timedelta(days=7)
    status = 'order placed'
    orders_data = [
        {
            'id': order.order.id,
            'product': {
                'name': order.product.name,
                'image': order.product.image1.url
            },
            'placed_at': order.order.order_at.strftime("%B %d, %Y"),
            'status': status,
            'expected_delivery': delivery.strftime("%B %d, %Y"),
        }
        for order in orders
    ]
    return render(request,'order/track_order.html',{'order':orders,'orders_json': json.dumps(orders_data, cls=DjangoJSONEncoder)})

def Cancel_order(request,order_id):
    order = Order.objects.get(id=order_id,user=request.user)
    order.is_canceled=True
    if order.is_canceled:
        order.delete()
    return redirect('track_order')



