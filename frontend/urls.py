from django.urls import path
from frontend import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('product-listing', views.ProductListingView.as_view(), name="ProductListingView"),
    path('product-listing/<product_category_id>', views.ProductListingView.as_view(), name="ProductListingView"),
    path('product-details/<int:product_id>', views.ProductDetailsView.as_view(), name="ProductDetailsView"),
    # path('checkout', views.Checkout.as_views())
]
