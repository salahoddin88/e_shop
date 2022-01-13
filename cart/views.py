from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from products.models import ProductCategory
from orders.models import Order, OrderDetails, Payment
from . models import Cart
import json
import datetime
import razorpay

@login_required
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


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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

    def post(self, request):

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        cartProducts = Cart.objects.filter(user=request.user)
        subTotal = 0
        total = 0
        shippingCost = 50
        for key, cartProduct in enumerate(cartProducts):
            productTotal = int(cartProduct.quantity) * int(cartProduct.product.price)
            total += productTotal
            subTotal += productTotal
        total = (shippingCost + subTotal) * 100

        client = razorpay.Client(auth=("rzp_test_DBRMtVnE1JvCM2", "vPRNJ7R1gJKlXvPUriFXqfHC"))
        receipt = f'order_rcptid{request.user.id}'
        data = {"amount": total, "currency": "INR", "receipt": receipt}
        payment = client.order.create(data=data)
        
        if payment.get('id'):
            context = {
                'order_id': payment['id'],
                'amount': payment['amount'],
                'first_name' : first_name,
                'last_name' : last_name,
                'address' : address,
            }
            return render(request, 'capture-payment.html', context)



class PaymentSuccess(View):
    def post(self, request):
        razorpay_payment_id  = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        cartProducts = Cart.objects.filter(user=request.user)

        if cartProducts:
            order = Order.objects.create(
                user = request.user,
                user_name=f'{first_name} {last_name}',
                user_address = address,
                razor_pay_order_id=razorpay_order_id
            )
            for cartProduct in cartProducts:
                OrderDetails.objects.create(
                    order=order,
                    product=cartProduct.product,
                    quantity=cartProduct.quantity,
                    price=cartProduct.product.price,
                )
            cartProducts.delete()
        
        return JsonResponse({'status':'success'})



@csrf_exempt
def RazorpayWebhook(request):
    requestBody = json.load(request.body.decode('utf-8'))
    payload = requestBody['payload']
    if payload['payment']:
        order_id = payload['payment']['entity']['order_id']
        try:
            order = Order.objects.get(razor_pay_order_id=order_id)
            payment = Payment.objects.get_or_create(order=order)
            payment.payment_id=payload['payment']['entity']['id']
            payment.payment_status=payload['payment']['entity']['status']
            payment.payment_method=payload['payment']['entity']['method']
            payment.created_at=payload['payment']['entity']['created_at']
            payment.amount=payload['payment']['entity']['amount']
            payment.save()
            order.payment_status=True
            order.save()
            return JsonResponse({'status':'success'})
        except:
            return JsonResponse({'status':'failed'})


def ThankYou(request):
    return HttpResponse('<h1>Thank You, Your order has been placed! </h1>')


