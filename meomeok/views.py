import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
# from django.contrib.auth.models import User

#random test
import random

# 레스토랑 모델 불러오기
from .models import Restaurant
from .serializers import RestaurantSerializer

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    restaurants_counts = Restaurant.objects.all().count()

    context = {
        'restaurants_counts': restaurants_counts,
    }

    return render(request, 'index.html', context = context)

class RestaurantListView(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.all() 
    template_name = 'meomeok/restaurant_list.html'
    paginate_by = 10
# random.random()

class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    def restaurant_detail_view(request, primary_key):
        restaurant = get_object_or_404(Restaurant, pk=primary_key)
        return render(request, 'memeok/restaurant_detail.html', context={'restaurant': restaurant})

# @csrf_exempt
# def restaurant_list(request):
#     if request.method == 'GET':
#         restaurants = Restaurant.objects.all()
#         serializer = RestaurantSerializer(restaurants, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = RestaurantSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def restaurant_detail(request, pk):
#     try:
#         restaurant = Restaurant.objects.get(pk=pk)
#     except Restaurant.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = RestaurantSerializer(restaurant)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = RestaurantSerializer(restaurant, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         restaurant.delete()
#         return HttpResponse(status=204)

# function based view via api
@api_view(['GET', 'POST'])
def restaurant_list(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
