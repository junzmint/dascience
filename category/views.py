from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import pandas as pd
import numpy as np
import random
from .Pet import getInsightPet
from .Health import getInsightHealth
from .ManFashion import getInsightManFashion

# Create your views here.
class CategoryView(View):
    def get(self, request):
        category = request.GET.get('category', 'unknown')
        cmt_type = request.GET.get('type', 'negative')

        data = {}
        if (category == "pet"):
            data = getInsightPet(cmt_type)
        elif (category == "health"):
            data = getInsightHealth(cmt_type)
        elif (category == "man_fashion"):
            data = getInsightManFashion(cmt_type)
        
        response_data = data
        return JsonResponse(response_data)
    
# Create functions to get word cloud here