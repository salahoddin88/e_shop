from django.db.models import Sum
from django import template
from cart.models import Cart


register = template.Library()

@register.simple_tag
def cartCount(request):
    """  Display cart count based on user's current session  """
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user).aggregate(cart_sum=Sum('quantity'))
        return carts['cart_sum']
    return 0


