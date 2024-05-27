from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import random

# Create your views here.
class CategoryView(View):
    def get(self, request):
        category = request.GET.get('category', 'unknown')
        random_number = random.randint(1, 10)
        response_data = {
            "category": category,
            "random_number": random_number
        }
        return JsonResponse(response_data)
    
# Create functions to get word cloud here