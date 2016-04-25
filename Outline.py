# CX 4242 Final Project
#
# run pip install googlemaps before running this
# also run pip install geopy

from googlemaps import Client
from geopy.geocoders import Nominatim
import json
import requests

#get latitude and longitude from pinging a website
#website uses ip address to calculate returned values
def GetLocation():
    url = "http://geoip.nekudo.com/api/"
    r = requests.get(url)
    j = json.loads(r.text)
    lat = j['location']['latitude']
    lon = j['location']['longitude']
    return((lat,lon))

#get latitude and longitude from user entered address
#format checking?
def GetAddressLocation(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    return((location.latitude, location.longitude))

'''
This function returns a list of nearby restaurants. Each entry in the list
is in the format (RestaurantName, distance)
parameters: latitude: string
            logitude: string
returns: list of tuples containing restaurant name and distance
'''
def GetNearbyRestaurants(latitude, logitude):
    restaurants = []
    #request to Google places API
    restaurants.append("Chick-fil-A", 13)
    return restaurants

'''
This function returns the nutrition facts of a restaurant
I am not sure what the nutrition information looks like

'''
def GetNutrition(restaurantName):
    #can you return this in this format please:
    '''
    [
      ["Restaurant Name", "Calories", "Distance", "Nutrition Fact Name", "Other Nutrition Fact Name"]
      [restaurantNameValue1, caloriesForThatRastaurant, NuttritionFact, ...]
      [restaurantNameValue2, ...]
    ]
    
    '''
    #if not its ok, just let me know how you are planning on returning it
    return []
    
