import geopy
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

if __name__ == '__main__':
    print(MyLocation())

