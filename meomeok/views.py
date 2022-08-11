from django.shortcuts import render, get_object_or_404
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