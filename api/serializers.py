from rest_framework import fields, serializers
from products.models import Product, ProductCategory
from cart.models import Cart

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_category', 'name', 'price', 'description', 'cover_image', 'sku', 'stock']
        depth = 1

