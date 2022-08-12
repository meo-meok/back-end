from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    # path('restaurants/<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/', views.restaurant_list),
    path('restaurants/<int:pk>', views.restaurant_detail),
]