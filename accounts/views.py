import datetime

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout
from django.contrib import messages
from order.models import Order, TransactionOrder
from .forms import RegisterForm, RestaurantRegisterForm, CreatUserForm
from .models import User, Restaurant, Customer


# Accessing Customer To profle
def check_customer(user):
    if user.roll == 1:
        return True
    return False


# Accessing Restaurant To profile
def check_restaurant(user):
    if user.roll == 2:
        return True
    return False


class Profile(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.roll == 1:
            return redirect('accounts:customer')
        elif request.user.roll == 2:
            return redirect('accounts:restaurant')
        elif request.user.roll is None and request.user.is_superuser:
            return redirect('accounts:admin_profile')


class CustomerProfile(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'accounts/customer_profile.html'

    def get(self, request):
        return render(request, self.template_name)

    def test_func(self):
        return check_customer(self.request.user)


class RestaurantProfile(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'accounts/restaurant_profile.html'

    def get(self, request):
        return render(request, self.template_name)

    def test_func(self):
        return check_restaurant(self.request.user)


class AdminProfile(LoginRequiredMixin, View):
    template_name = 'accounts/admin_profile.html'

    def get(self, request):
        return render(request, self.template_name)


class LogoutUserView(View):

    def get(self, request):
        logout(request)
        return redirect('login')


class Register(View):
    template_name = 'accounts/user_register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form = form.save(commit=False)
            form.roll = 1
            form.save()
            Customer.objects.create(user=form.user, address=cd['address'])
            return redirect('login')

        return render(request, self.template_name, {'form': form})


class RestaurantRegister(View):
    template_name = 'accounts/restaurant_register.html'
    form_class = RestaurantRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['name'], password=cd['password'])
            user.roll = 2
            # Restaurant.objects.create(user=user, name=cd['name'], restaurant_type=cd['type'], start_time=cd['start_time'], finish_time=cd['finish_time'],
            #                           shipping_time=cd['shipping_time'])
            form.user = user
            form.save()
            return redirect('login')

        return render(request, self.template_name, {'form': form})


class AddAdminCustomer(LoginRequiredMixin, View):
    template_name = 'accounts/admin_create_customer.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = form.save(commit=False)
            user.roll = 1
            user.save()
            Customer.objects.create(user=user, address=cd['address'])
            messages.success(request, 'Customer Created')
            return redirect('accounts:add_customer')

        return render(request, self.template_name, {'form': form})


class AddAdminRestaurant(LoginRequiredMixin, View):
    template_name = 'accounts/admin_create_restaurant.html'
    form_class = RestaurantRegisterForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            form = form.save(commit=False)
            user = User.objects.create_user(username=cd['username'], password=cd['password1'], roll=2)

            form.user = user
            form.save()
            messages.success(request, 'Customer Created')
            return redirect('accounts:add_restaurant')

        return render(request, self.template_name, {'form': form})


class CompanyEarnView(LoginRequiredMixin, View):
    template_name = 'accounts/earn.html'
    context = {}

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.restaurants = Restaurant.objects.all()
        self.orders = TransactionOrder.objects.all()
        self.total_order = self.orders.count()

    def get(self, request):

        revenue_shipping = 0
        revenue_food = 0
        for company in self.orders:
            revenue_food += company.admin_share
            revenue_shipping += company.shipping_cost_admin
        total_revenue = revenue_food + revenue_shipping
        current_month_revenue = 0
        current_month = self.orders.filter(created__month=datetime.datetime.now().month)

        for current in current_month:
            current_month_revenue += current.admin_share

        self.context['orders'] = self.orders
        self.context['total_order'] = self.total_order
        self.context['total_revenue'] = total_revenue
        self.context['current_month_revenue'] = current_month_revenue
        self.context['restaurants'] = self.restaurants
        self.context['revenue_food'] = revenue_food
        self.context['revenue_shipping'] = revenue_shipping

        return render(request, self.template_name, self.context)

    def post(self, request):

        if request.POST.get('restaurant') and request.POST.get('time'):
            date = request.POST.get('time')
            restaurant = request.POST.get('restaurant')
            orders = TransactionOrder.objects.filter(created__date=date, order__vendor__name=restaurant)
            self.context['orders'] = orders

        elif request.POST.get('time'):
            revenue_food = 0
            revenue_shipping = 0
            date = request.POST.get('time')
            orders = TransactionOrder.objects.filter(created__date=date)
            for order in orders:
                revenue_food += order.admin_share
                revenue_shipping += revenue_shipping

            self.context['revenue_food'] = revenue_food
            self.context['revenue_shipping'] = revenue_shipping

        return render(request, self.template_name, self.context)
