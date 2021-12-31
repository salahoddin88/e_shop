from django.shortcuts import render, redirect
from . models import Cart
from django.views import View
from products.models import ProductCategory, Product
from django.http import HttpResponse

def addToCart(request):

    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))

    cart, isCraeted = Cart.objects.get_or_create(user=request.user, product_id=product_id)
    if isCraeted:
        cart.quantity = quantity
    else:
        cart.quantity = quantity + cart.quantity
    cart.save()

    # Traditional Approach
    # try:
    #     checkCart = Cart.objects.get(user=request.user, product_id=product_id)
    #     checkCart.quantity = checkCart.quantity + quantity
    #     checkCart.save()
    # except Cart.DoesNotExist:

    #     Cart.objects.create(
    #         user=request.user,
    #         product_id=product_id,
    #         quantity=quantity
    #     )

    return redirect('ProductDetailsView', product_id=product_id)


class MyCart(View):
    
    template_name = 'my-cart.html'

    def get(self, request):
        productCategories = ProductCategory.objects.filter(status=True)
        cartProducts = Cart.objects.filter(user=request.user)

        carts = {}
        subTotal = 0
        total = 0
        shippingCost = 50
        for key, cartProduct in enumerate(cartProducts):
            productTotal = int(cartProduct.quantity) * int(cartProduct.product.price)
            total += productTotal
            subTotal += productTotal
            carts[key] = {
                'product_image': cartProduct.product.cover_image,
                'product_name': cartProduct.product.name,
                'product_price': cartProduct.product.price,
                'quantity': cartProduct.quantity,
                'productTotal': productTotal,
                'cart_id': cartProduct.id
            }

        total = shippingCost + subTotal
        carts = list(carts.values())
        context = {
            'productCategories': productCategories,
            'cartProducts': carts,
            'subTotal':subTotal,
            'shippingCost': shippingCost,
            'total':total,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        cartIds = request.POST.getlist('cart_id')
        quantites = request.POST.getlist('quantity')
        for cartKey, cartId in enumerate(cartIds):
            try:
                cartObject = Cart.objects.get(id=cartId)
                if quantites[cartKey] == '0':
                    cartObject.delete()
                else:
                    cartObject.quantity = quantites[cartKey]
                    cartObject.save()
            except Cart.DoesNotExist:
                pass
        
        return redirect('MyCart')


class Checkout(View):
    template_name = 'checkout.html'

    def get(self, request):
        productCategories = ProductCategory.objects.filter(status=True)
        cartProducts = Cart.objects.filter(user=request.user)
        carts = {}
        subTotal = 0
        total = 0
        shippingCost = 50
        for key, cartProduct in enumerate(cartProducts):
            productTotal = int(cartProduct.quantity) * int(cartProduct.product.price)
            total += productTotal
            subTotal += productTotal
            carts[key] = {
                'product_name': cartProduct.product.name,
                'productTotal': productTotal,
            }

        total = shippingCost + subTotal
        carts = list(carts.values())
        context = {
            'productCategories': productCategories,
            'cartProducts': carts,
            'subTotal': subTotal,
            'shippingCost': shippingCost,
            'total': total,
        }
        return render(request, self.template_name, context)
