from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Profile.as_view(), name='profile'),
    path('customer/', views.CustomerProfile.as_view(), name='customer'),
    path('restaurant/', views.RestaurantProfile.as_view(), name='restaurant'),
    path('admin_panel/', views.AdminProfile.as_view(), name='admin_profile'),
    path('signup/', views.Register.as_view(), name='signup'),
    path('restauran-singup', views.RestaurantRegister.as_view(), name='restaurant_signup'),
    path('logout-user/', views.LogoutUserView.as_view(), name='user_logout'),
    path('add_customer/', views.AddAdminCustomer.as_view(), name='add_customer'),
    path('add_restaurant/', views.AddAdminRestaurant.as_view(), name='add_restaurant'),
    path('earn/', views.CompanyEarnView.as_view(), name='earn'),
]