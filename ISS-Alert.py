import requests
import unicornhat
from geopy.geocoders import Nominatim
from time import sleep
geolocator = Nominatim()
ISS = "http://api.open-notify.org/iss-now.json"
#My location
home = geolocator.geocode("Blackpool UK")
home_lat = home.latitude
home_lat = float(home_lat)
home_lon = home.longitude
home_lon = float(home_lon)
print("HOME")
print(home_lat, home_lon)



while True:
    r = requests.get(ISS)
    lat = float(r.json()['iss_position']['latitude'])
    lon = float(r.json()['iss_position']['longitude'])
    #lat = float(53.8182212)
    #lon = float(-3.0564845)
    print(lat, lon)
    if lat >= (home_lat -1) and lat <= (home_lat) and lon >= (home_lon -1) and lon <= (home_lon):
        print("WARNING: ISS IS ALMOST OVERHEAD")
        for x in range(8):
            for y in range(8):
                unicornhat.set_pixel(x,y,255,0,0)
                sleep(0.01)
                unicornhat.show()
        sleep(15)
        unicornhat.clear()
        unicornhat.show()
        sleep(45)
    else:
        print("ISS NOT NEAR")
        for x in range(8):
            for y in range(8):
                unicornhat.set_pixel(x,y,0,255,0)
                sleep(0.01)
                unicornhat.show()
        sleep(15)
        unicornhat.clear()
        unicornhat.show()
        sleep(45)
