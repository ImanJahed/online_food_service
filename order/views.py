import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from accounts.models import Restaurant, Customer
from accounts.views import check_customer
from order.forms import OrderForm
from order.models import Order, TransactionOrder
from restaurant.models import Food
import utils


# Create your views here.

class PlaceOrder(LoginRequiredMixin, View):
    template_name = 'order/place_order.html'

    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        context = {
            'food': food
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        restaurant = Restaurant.objects.get(pk=food.vendor.pk)
        total_price = food.price

        shipping_cost = restaurant.shipping_cost

        shipping_cost_admin = restaurant.shipping_cost * 0.2 + restaurant.shipping_cost
        shipping_cost_restaurant = restaurant.shipping_cost * 0.8 + restaurant.shipping_cost

        restaurant_share = total_price * 0.96
        admin_share = total_price * 0.04

        order_id = utils.generate_order_id()
        order = Order.objects.create(vendor=restaurant, user=request.user.customer, food=food, shipping_cost=shipping_cost,
                                     total_price=total_price, restaurant_share=restaurant_share, admin_share=admin_share,
                                     order_id=order_id)
        all_order = Order.objects.all()
        total_admin_share = 0
        total_restaurant_share = 0
        for share in all_order:
            total_admin_share += (share.admin_share + shipping_cost_admin)
            total_restaurant_share += (share.restaurant_share + shipping_cost_restaurant)

        TransactionOrder.objects.create(order=order, total_order=order.total_price, shipping_cost_admin=shipping_cost_admin,
                                        shipping_cost_restaurant=shipping_cost_restaurant,
                                        restaurant_share=order.restaurant_share, admin_share=order.admin_share,
                                        total_admin_share=total_admin_share, total_restaurant_share=total_restaurant_share)

        return redirect('restaurant:restaurant_detail', pk=food.vendor.pk)


class OrderDetailView(LoginRequiredMixin, View):
    template_name = 'order/order_detail.html'
    form_class = OrderForm

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = self.form_class(instance=order)
        context = {
            'order': order,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, reqeust, pk):
        order = get_object_or_404(Order, pk=pk)
        form = self.form_class(reqeust.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order:order_detail', order.id)

        return render(reqeust, self.template_name, {'form': form})


class CustomerOrderDetail(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'order/customer_order_detail.html'

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        context = {
            'order': order
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect('accounts:customer')


    def test_func(self):
        return check_customer
