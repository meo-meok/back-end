from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
#random test
import random

# 레스토랑 모델 불러오기
from .models import Restaurant

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    restaurants_counts = Restaurant.objects.all().count()

    context = {
        'restaurants_counts': restaurants_counts,
    }

    return render(request, 'index.html', context = context)

