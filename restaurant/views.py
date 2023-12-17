from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import Restaurant
from order.models import TransactionOrder
from restaurant.forms import FoodItemForm

from accounts.views import check_restaurant
from .models import Food
from django.template.defaultfilters import slugify


# Create your views here.
class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant/restaurant_list.html'
    context_object_name = 'restaurants'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = datetime.now().time()
        out_time = current_time.strftime("%H")
        context['time_now'] = out_time
        return context


class RestaurantDetailView(View):
    template_name = 'restaurant/restaurant_detail.html'

    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        foods = Food.objects.filter(vendor=restaurant, is_available=True)
        context = {
            'restaurant': restaurant,
            'foods': foods
        }
        return render(request, self.template_name, context)


class AddFood(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'restaurant/add_food.html'
    form_class = FoodItemForm

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        try:
            self.vendor = Restaurant.objects.get(user=request.user)
        except:
            return None

    def get(self, request):
        form = self.form_class()

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            foodtitle = form.cleaned_data['food_title']
            food = form.save(commit=False)
            food.vendor = self.vendor
            food.slug = slugify(foodtitle)
            form.save()

            return redirect('restaurant:add_food')
        return render(request, self.template_name, {'form': form})

    def test_func(self):
        return check_restaurant


class ListFoodView(View):
    template_name = 'restaurant/list_food.html'

    def get(self, request):
        foods = Food.objects.filter(vendor__user=request.user)
        return render(request, self.template_name, {'foods': foods})


class EditFoodView(View):
    template_name = 'restaurant/edit_food.html'
    form_class = FoodItemForm

    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        form = self.form_class(instance=food)
        context = {
            'food': food,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        form = self.form_class(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('restaurant:list_food')

        return render(request, self.template_name, {'form': form})


class RestaurantEarnView(LoginRequiredMixin, View):
    template_name = 'restaurant/restaurant_earn.html'
    context = {}

    def get(self, request):
        restaurant = Restaurant.objects.get(user=request.user)
        orders = TransactionOrder.objects.filter(order__vendor=restaurant)

        total_order = orders.count()

        revenue_shipping = 0
        revenue_food = 0
        for res in orders:
            revenue_food += res.restaurant_share
            revenue_shipping += res.shipping_cost_restaurant

        total_revenue = revenue_food + revenue_shipping

        current_month_revenue = 0
        current_month = orders.filter(created__month=datetime.now().month)
        for current in current_month:
            current_month_revenue += current.restaurant_share

        self.context['orders'] = orders
        self.context['total_order'] = total_order
        self.context['total_revenue'] = total_revenue
        self.context['current_month_revenue'] = current_month_revenue
        self.context['restaurants'] = restaurant
        self.context['revenue_food'] = revenue_food
        self.context['revenue_shipping'] = revenue_shipping

        return render(request, self.template_name, self.context)

    def post(self, request):
        if request.POST.get('restaurant') and request.POST.get('time'):
            date = request.POST.get('time')
            restaurant = request.POST.get('restaurant')
            orders = TransactionOrder.objects.filter(created__date=date, order__vendor__name=restaurant)

        elif request.POST.get('time'):
            revenue_food = 0
            revenue_shipping = 0
            date = request.POST.get('time')
            orders = TransactionOrder.objects.filter(created__date=date)
            for order in orders:
                revenue_food += order.admin_share
                revenue_shipping += revenue_shipping

        self.context["orders"] = orders
        self.context["total_order"] = orders.count()
        self.context['revenue_food'] = revenue_food
        self.context['revenue_shipping'] = revenue_shipping
        return render(request, self.template_name, self.context)
