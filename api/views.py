from rest_framework import viewsets, filters, authentication
from . import serializers, permissions
from products.models import Product, ProductCategory
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserAuthView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProductView(viewsets.ModelViewSet):
    permission_classes = (permissions.GetRequestOnly, )
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('product_category__id', )
    ordering_fields = ('price', )


class ProductCategoryView(viewsets.ModelViewSet):
    serializer_class = serializers.ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    

