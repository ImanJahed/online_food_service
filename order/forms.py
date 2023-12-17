from django import forms

from .models import Order, TransactionOrder


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['status']
