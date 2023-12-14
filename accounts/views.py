from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Profile(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.roll == 1:
            return redirect('accounts:customer')
        elif request.user.roll == 2:
            return redirect('accounts:restaurant')
        elif request.user.roll is None and request.user.is_superuser:
            return redirect('accounts:admin_profile')


class CustomerProfile(LoginRequiredMixin, View):
    template_name = 'accounts/customer_profile.html'

    def get(self, request):

        return render(request, self.template_name)


class RestaurantProfile(LoginRequiredMixin, View):
    template_name = 'accounts/restaurant_profile.html'

    def get(self, request):
        return render(request, self.template_name)


class AdminProfile(LoginRequiredMixin, View):
    template_name = 'accounts/admin_profile.html'

    def get(self, request):
        return render(request, self.template_name)

