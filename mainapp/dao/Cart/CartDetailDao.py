from mainapp.model.CartDetail import CartDetail
from datetime import datetime
from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings
from django.utils import timezone

def get_cart_detail_by_cart_detail_id(cart_detail_id):
    """
    Get cart detail by cart detail id
    """
    cart_item = CartDetail.objects.get(pk=cart_detail_id)
    return cart_item

def get_cart_detail_by_cart_id(cart_id):
    """
    Get cart detail by cart id
    """
    list_cart_item = CartDetail.objects.filter(cart_id=cart_id).order_by('cart_detail_id')
    return list_cart_item

def get_cart_detail_by_pk_product_detail_id(cart_id, product_detail_id):
    """
    Get cart detail by pk, product detail id
    """
    cart_detail = CartDetail.objects.filter(cart_id=cart_id, product_detail_id=product_detail_id).first()
    return cart_detail

def count_cart_detail_by_cart_id(cart_id):
    """
    Count cart detail by cart id
    """
    count_cart_item = CartDetail.objects.filter(cart_id=cart_id).count()
    return count_cart_item

def insert_cart_detail(cart_detail):
    """
    Insert cart detail
    """
    c_detail = CartDetail(cart_id=cart_detail.cart_id,
                        product_detail_id=cart_detail.product_detail_id,
                        quantity=cart_detail.quantity)
    c_detail.save()
    return c_detail
def update_cart_detail(cart_detail_id, quantity):
    """
    Update quantity in cart detail
    """
    cart_detail = CartDetail.objects.get(pk=cart_detail_id)
    cart_detail.quantity = quantity
    cart_detail.save()
    return cart_detail

def add_quantity_cart_detail(cart_detail_id, quantity):
    """
    Update quantity in cart detail
    """
    cart_detail = CartDetail.objects.get(pk=cart_detail_id)
    cart_detail.quantity = cart_detail.quantity + quantity
    cart_detail.save()
    return cart_detail

def delete_cart_detail(cart_detail_id):
    """
    Delete cart detail
    """
    cart_detail = CartDetail.objects.get(pk=cart_detail_id)
    cart_detail.delete()
