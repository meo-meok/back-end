from django.shortcuts import render
from rest_framework import generics

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Restaurant
from .serializers import RestaurantSerializer


class ListRestaurant(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer = RestaurantSerializer

class DetailRestaurant(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer = RestaurantSerializer


@csrf_exempt
def RestaurantAPI(request, id = 0) :
    if request.method == 'GET' :
        objset = Restaurant.objects.all()
        objset_serializer = RestaurantSerializer(objset)
        return JsonResponse(objset_serializer, safe = False)
    elif request.method == 'POST' :
        data = JSONParser().parse(request)
        serializer = RestaurantSerializer(data = data)
        if serializer.is_valid() :
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    