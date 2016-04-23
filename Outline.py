#run pip install googlemaps before running this
from googlemaps import Client


'''
https://developers.google.com/maps/documentation/geolocation/intro#overview
This function gets the latitute and logitude values
params: none
returns: tuple: (string, string): (latitude, logitude) of current location
'''
def GetLocation():
    #connect with google geolocation API
    #The Google Maps Geolocation API key
    #geo_api_key = 
    return (0, 0)

'''
This function gets the latitude and logitude of an address
returns: tuple: (string, string): (latitude, logitude) of address
'''
def GetAddressLocation(address):
    #google geologation API
    gmaps = Client(gmaps_api_key)
    lat, lng = gmaps.address_to_latlng(address)
    return (0, 0)

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
    return {}
    
