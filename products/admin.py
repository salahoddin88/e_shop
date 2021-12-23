from django.contrib import admin
from products.models import ProductCategory, Product, ProductImages
from orders.models import Reviews

class ProductCategoryAdmin(admin.ModelAdmin):
    """ show columns as per list display tupples """
    list_display = ('name', 'status')

admin.site.register(ProductCategory, ProductCategoryAdmin)


# class ProductImagesAdmin(admin.StackedInline):
#     model = ProductImages

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    classes = ('collapse', )



class ProductReviewAdmin(admin.TabularInline):
    model = Reviews
    classes = ('collapse', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sku', 'product_category', 'status')
    inlines = (ProductImagesAdmin, ProductReviewAdmin)
    

admin.site.register(Product, ProductAdmin)





# admin.site.register(ProductImages)


