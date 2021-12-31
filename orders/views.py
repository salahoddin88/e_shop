from django.shortcuts import render
from django.views import View
# Create your views here.


class MyOrders(View):
    """ Display all placed order of logged in user """

    template_name = ""
    def get(self, request):
        context = None
        return render(request, self.template_name, context)


class OrderDetails(View):
    """ Display Order details of selected order_id """

    template_name = ""
    def get(self, request, order_id):
        context = None
        return render(request, self.template_name, context)
