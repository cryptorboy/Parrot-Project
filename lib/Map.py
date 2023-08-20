from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import requests
import json
import webbrowser as web

def MyLocation():
    try:
        url = 'https://www.google.com/maps/@12.9654586,77.6726256,10.25z?entry=ttu'
        web.open(url)
        response = requests.get("https://api.ipify.org").text
        url = 'https://get.geojs.io/v1/ip/geo/' + response + '.json'
        geo_q = requests.get(url)
        data = geo_q.json()

        state = data['city']

        country = data['country']

        return state, country
    except Exception as e:
        print(e)


def GoogleMap(place):
    url_place = "https://www.google.com/maps/place/" + str(place)

    # from geopy.geocoders import Nominatim
    # from geopy.distance import geodesic

    # # Initialize the geocoder
    # geolocator = Nominatim(user_agent="my_geocoder")

    # # Example place names for current location and target location
    # current_place = "San Francisco, CA"
    # target_place = "Los Angeles, CA"

    # # Geocode the place names to get latitude and longitude
    # current_location = geolocator.geocode(current_place)
    # target_location = geolocator.geocode(place)

    # # Check if geocoding was successful
    # if current_location is not None and target_location is not None:
    #     current_coords = (current_location.latitude, current_location.longitude)
    #     target_coords = (target_location.latitude, target_location.longitude)
        
    #     distance = geodesic(current_coords, target_coords).kilometers
    #     print(f"Distance between {current_place} and {place}: {distance:.2f} kilometers")
    # else:
    #     print("Geocoding failed for one or both place names.")

    geolocator = Nominatim(user_agent="my_Geocoder")

    location = geolocator.geocode(place, addressdetails= True)

    target_latlon = location.latitude , location.longitude

    location = location.raw['address']
    location = {
                'city': location.get('city',''),
                'state': location.get('state',''),
                'country': location.get('country','')
    }

    current_loc = geocoder.ip('me')

    current_lotlon = current_loc.latlng

    distance = str(great_circle(current_lotlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)

    web.open(url_place)
    return distance

if __name__ == '__main__':
    # print(MyLocation())
    print(GoogleMap("paris"))

