from .models import CartItem
from Products.models import Product


def add_to_cart(user,product_id,quantity=1):
    product=Product.objects.get(id=product_id)
    item,created = CartItem.objects.get_or_create(user = user,product=product)
    if not created:
        item.quantity+=quantity
        item.save()
        return item,False
    return item,True

def update_to_cart(user,product_id,action):
    item = CartItem.objects.get(user=user,product_id=product_id)
    if action == 'increase':
        quantity = 1
        item.quantity += quantity
        item.save()
    elif action == 'decrease':
        quantity = 1
        item.quantity -= quantity
        item.save()
    return item

def delete_to_cart(user,product_id):
    item = CartItem.objects.get(user=user,product_id=product_id)
    item.delete()

def cart_items(user):
    return CartItem.objects.filter(user=user).select_related('product')

def cart_count(user):
    return CartItem.objects.filter(user).count()
    