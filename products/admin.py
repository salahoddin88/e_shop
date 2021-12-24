from django.contrib import admin, messages
from products.models import ProductCategory, Product, ProductImages
from orders.models import Reviews


def activeStatus(modeladmin, request, queryset):
    queryset.update(status=True)
    messages.success(
        request, 'Selected record(s) marked as Active successfully!')


def inactiveStatus(modeladmin, request, queryset):
    queryset.update(status=False)
    messages.success(
        request, 'Selected record(s) marked as Inactive successfully!')


class ProductCategoryAdmin(admin.ModelAdmin):
    """ show columns as per list display tupples """
    list_display = ('name', 'status')
    list_filter = ('status', )
    actions = (activeStatus, inactiveStatus)

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
    list_filter = ('product_category', 'status')
    search_fields = ('name', 'price', 'sku')
    actions = (activeStatus, inactiveStatus)

admin.site.register(Product, ProductAdmin)





# admin.site.register(ProductImages)


