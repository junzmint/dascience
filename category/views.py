from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import pandas as pd
import numpy as np
import random
from .Pet import getInsightPet
# Create your views here.
class CategoryView(View):
    def get(self, request):
        category = request.GET.get('category', 'unknown')
        data = {}
        if (category == "pet"):
            data = getInsightPet()
        
        response_data = {
            "data": data,
        }
        return JsonResponse(response_data)
    
# Create functions to get word cloud here