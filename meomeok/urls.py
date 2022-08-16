from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    # path('restaurants/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    # path('restaurants/', views.restaurant_list), #api_view
    # path('restaurants/<int:pk>/', views.restaurant_detail), #api_view
    path('restaurants/', views.RestaurantList.as_view()), #classview
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view()), #classview
]

urlpatterns = format_suffix_patterns(urlpatterns)