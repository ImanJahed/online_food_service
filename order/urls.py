from django.urls import path

from . import views


app_name = 'order'


urlpatterns = [
    path('place_order/<int:pk>/', views.PlaceOrder.as_view(), name='place_order'),
    path('order-detail/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('customer_order_detail/<int:pk>/', views.CustomerOrderDetail.as_view(), name='customer_order_detail'),
]
