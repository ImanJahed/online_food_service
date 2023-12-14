from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Profile.as_view(), name='profile'),
    path('customer/', views.CustomerProfile.as_view(), name='customer'),
    path('restaurant/', views.RestaurantProfile.as_view(), name='restaurant'),
    path('admin_panel/', views.AdminProfile.as_view(), name='admin_profile')
]