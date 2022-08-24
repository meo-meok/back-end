from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('restaurants/', views.RestaurantListView.as_view(), name='restaurants'),
    # path('restaurants/<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/', views.restaurant_list),
    path('restaurants/<int:pk>', views.restaurant_detail),
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>', views.ReviewDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)