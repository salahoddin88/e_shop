from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductView)
router.register('product-categories', views.ProductCategoryView)
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.UserAuthView.as_view()),
    path('carts', views.CartView.as_view()),
    path('carts/<int:cartId>', views.CartView.as_view()),
    path('checkout', views.Checkout.as_view()),
]
