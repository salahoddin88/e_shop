from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductView)
router.register('product-categories', views.ProductCategoryView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.UserAuthView.as_view()),
]
