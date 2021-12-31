from django.shortcuts import render, redirect
from django.views import View
from products.models import ProductCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as AuthLogin, logout as AuthLogout


class Login(View):
    template_name  = 'login.html'
    form_class = AuthenticationForm
    productCategories = ProductCategory.objects.filter(status=True)

    def get(self, request):
        form = self.form_class()
        context = {
            'productCategories': self.productCategories,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        redirectURL = request.GET.get('next')
        if form.is_valid():
            AuthLogin(request, form.get_user())
            if redirectURL:
                return redirect(redirectURL)
            return redirect('home_page')
        context = {
            'productCategories': self.productCategories,
            'form': form
        }
        return render(request, self.template_name, context)


def logout(request):
    AuthLogout(request)
    return redirect('home_page')
