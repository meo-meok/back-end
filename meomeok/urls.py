from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListRestaurant.as_view()),
    path('<int:pk>/', views.DetailRestaurant.as_view()),
]