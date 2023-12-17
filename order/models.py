import random
import string

from django.db import models
from django.shortcuts import redirect

from accounts.models import Restaurant, Customer
from restaurant.models import Food


# Create your models here.
class Order(models.Model):
    class StatusChoice(models.TextChoices):
        initial = 'Initial'
        papering = 'Papering'
        sending = 'Sending'
        canceled = 'Canceled'

    vendor = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='vendor_order')
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='user_order')
    order_id = models.CharField(max_length=15)
    total_price = models.IntegerField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='order_food')
    status = models.CharField(max_length=50, choices=StatusChoice, default=StatusChoice.initial)
    order_time = models.DateTimeField(auto_now_add=True)
    shipping_cost = models.IntegerField()
    restaurant_share = models.IntegerField()
    admin_share = models.IntegerField()
    auto_or_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.vendor} - {self.user.user.username} - {self.order_id}'

    def get_absolute_url(self):
        return redirect('order:order_detail', kwargs={'pk': self.order.id})


class TransactionOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    total_order = models.IntegerField()
    shipping_cost_admin = models.IntegerField()
    shipping_cost_restaurant = models.IntegerField()
    restaurant_share = models.IntegerField()
    admin_share = models.IntegerField()
    total_restaurant_share = models.IntegerField()
    total_admin_share = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.order_id
