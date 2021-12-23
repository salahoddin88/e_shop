from django.urls import path
from frontend import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('product-listing/<int:product_category_id>', views.ProductListingView.as_view(), name="ProductListingView"),
    path('product-details/<int:product_id>', views.ProductDetailsView.as_view(), name="ProductDetailsView")
]