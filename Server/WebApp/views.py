from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def GetMyLocation():
    return "33.7769380", "-84.3930570"
def GetRestaurantsNearMe(latitude, logitude):
    return [("Chick-fil-A", 20), ("MacDonolds", 10), ("Flying Biscuit", 10)]

def GetNutrition(restaurantName):
    nutrition = {}
    nutrition["calories"] = 200
    return nutrition
def GetNutritionFacts():
    d = []
    d.append(["Restaurant Name", "distance", "calories"])
    d.append(["Chick-fil-A", 20, 200])
    d.append(["Farm Burger burger", 14, 400])
    return d

# Create your views here.
def index(request):
    data = GetNutritionFacts()
    header_names = data[0]
    restaurant_list = data[1:]
    template = loader.get_template('WebApp/index.html')
    context = {'restaurant_list': restaurant_list
    , 'header_names': header_names,}

    return HttpResponse(template.render(context, request))
