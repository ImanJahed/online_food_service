from restaurant.models import Restaurant
from .models import Customer


def get_vendor(request):
    try:
        vendor = Restaurant.objects.get(user=request.user)
    except:
        vendor = None
    return dict(vendor=vendor)


def get_customer(request):
    try:
        user_profile = Customer.objects.get(user=request.user)
    except:
        user_profile = None
    return dict(user_profile=user_profile)