from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def create_cart(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def cart_home(request):
    # get the products
    pr = Product.objects.all()
    cart_id = request.session.get("cart_id", None)
    print(cart_id)
    # check if the cart with that id exits or not
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        # if exits
        cart_obj = qs.first()
        # check if the user is logged in or empty session or guest
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        # create cart
        cart_obj = create_cart()
        request.session['cart_id'] = cart_obj.id
    return render(request, 'cart/index.html', {'pr': pr})

def add_to_cart(request, slug):
    # current session cart id
    current_id = request.session['cart_id']
    product = Product.objects.get(slug=slug)
    # add to cart
    cart = Cart.objects.get(id=current_id)
    
    # to add in many to many field
    cart.products.add(product)

    cart.total += product.price
    cart.save()
    return redirect("cart_home")
    print("Done")

# update cart
def delete_cart_single(request, product_id):
    current_id = request.session['cart_id']
    product_obj = Product.objects.get(id=product_id)
    cart_obj = Cart.objects.get(id=current_id)

    # delete from cart
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
        # decrease the price
        cart_obj.total -= product_obj.price
        cart_obj.save()
        return redirect("cart_home")
    else:
        return redirect("cart_home")