from django.shortcuts import render, redirect
from django.views import View
from products.models import ProductCategory, Product


def home_page(request):
    productCategories = ProductCategory.objects.filter(status=True)
    latestProductCategories = ProductCategory.objects.filter(status=True).order_by('-id')[:5]
    context = {
        'productCategories': productCategories,
        'latestProductCategories': latestProductCategories
    }
    return render(request, 'home-page.html', context)



class ProductListingView(View):
    
    def get(self, request, product_category_id=None):
        productCategories = ProductCategory.objects.filter(status=True)
        products = Product.objects.filter(status=True, product_category_id=product_category_id)
        context = {
            'productCategories': productCategories,
            'products': products
        }
        return render(request, 'product-listing.html', context)



class ProductDetailsView(View):

    def get(self, request, product_id=None):
        productCategories = ProductCategory.objects.filter(status=True)
        productDetails = Product.objects.get(id=product_id)
        relatedProducts = Product.objects.filter(status=True, product_category_id=productDetails.product_category_id).exclude(id=product_id)
        context = {
            'productCategories':  productCategories,
            'productDetails': productDetails,
            'relatedProducts': relatedProducts
        }
        return render(request, 'product-details.html', context)
