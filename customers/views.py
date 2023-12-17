# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required
# # from accounts.forms import UserInfoForm, UserProfileForm
# from accounts.models import UserProfile
# from django.contrib import messages
# from orders.models import Order, OrderedFood
# import simplejson as json





# def my_orders(request):
#     orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
#
#     context = {
#         'orders': orders,
#     }
#     return render(request, 'customers/my_orders.html', context)
#
#
# def order_detail(request, order_number):
#     try:
#         order = Order.objects.get(order_number=order_number, is_ordered=True)
#         ordered_food = OrderedFood.objects.filter(order=order)
#         subtotal = 0
#         for item in ordered_food:
#             subtotal += (item.price * item.quantity)
#
#         context = {
#             'order': order,
#             'ordered_food': ordered_food,
#             'subtotal': subtotal,
#
#         }
#         return render(request, 'customers/order_detail.html', context)
#     except:
#         return redirect('customer')

# Create your views here.
