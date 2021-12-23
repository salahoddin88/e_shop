from django.contrib import admin
from orders.models import Order, OrderDetails


# class OrderDetailsAdmin(admin.StackedInline):
#     model = OrderDetails

class OrderDetailsAdmin(admin.TabularInline):
    model = OrderDetails


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'order_status', 'payment_status')
    inlines = (OrderDetailsAdmin, )

admin.site.register(Order, OrderAdmin)


