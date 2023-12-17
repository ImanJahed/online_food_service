from django.urls import path

from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('add_food/', views.AddFood.as_view(), name='add_food'),
    path('restaurant_earn/', views.RestaurantEarnView.as_view(), name='restaurant_earn'),
    path('list_food/', views.ListFoodView.as_view(), name='list_food'),
    path('edit_food/<int:pk>/', views.EditFoodView.as_view(), name='edit_food'),
]
