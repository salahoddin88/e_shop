from django.shortcuts import render
from django.views import View
from .import forms as UserForm


class UserProfile(View):
    """ Update User Profile of logged in user  """
    template_name = ""
    form_class = UserForm.UpdateProfileForm

    def get(self, request):
        form = self.form()
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)