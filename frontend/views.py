from django.shortcuts import render, redirect
from django.views import View
from products.models import ProductCategory, Product
from django.contrib.auth import login
from django.contrib.auth.models import User


#Assignments 
""" maintain stocks """
""" Make Logo and title Dynamic : Create new app website setting Note:Use get_or_create(id=1) """

def home_page(request):
    productCategories = ProductCategory.objects.filter(status=True)
    latestProductCategories = ProductCategory.objects.filter(status=True).order_by('-id')[:5]
    context = {
        'productCategories': productCategories,
        'latestProductCategories': latestProductCategories,
    }
    return render(request, 'home-page.html', context)



class ProductListingView(View):
    
    def get(self, request, product_category_id=None):
        productCategories = ProductCategory.objects.filter(status=True)
        search = request.GET.get('search')
        sorting = request.GET.get('sorting')
        minPrice = request.GET.get('min')
        maxPrice = request.GET.get('max')

        searchDict = {
            'status': True
        }

        if minPrice:
            minPrice = int(minPrice.replace('$',''))
            searchDict['price__gte'] = minPrice

        if maxPrice:
            maxPrice = int(maxPrice.replace('$',''))
            searchDict['price__lte'] = maxPrice
            
        if product_category_id and product_category_id != 'None':
            searchDict['product_category_id'] = product_category_id

        if search:
            searchDict['name__contains'] = search
        
        if sorting == "low":
            products = Product.objects.filter(**searchDict).order_by('price')
        elif sorting == 'high':
            products = Product.objects.filter(**searchDict).order_by('-price')
        else:
            products = Product.objects.filter(**searchDict)
        context = {
            'productCategories': productCategories,
            'products': products,
            'product_category_id': product_category_id
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
        # user = User.objects.get(id=2)
        # login(request, user)
        return render(request, 'product-details.html', context)



def test_login(request):
    user = User.objects.get(id=2)
    login(request, user)
    print(request.user)

    if request.user.is_authenticated:
        print("Hello")
    else:
        print("Not loggedIn")

