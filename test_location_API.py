import googlemaps
import pandas as pd
import time
from geopy.geocoders import Nominatim

def miles_to_meter(miles):
    try:
        return miles * 1609.344
    except:
        return 0

API_KEY = open('API_KEY.txt','r').read()
map_client = googlemaps.Client(API_KEY)

geolocator = Nominatim(user_agent="receptionist")
location = geolocator.geocode("Ottawa")

location = (location.latitude, location.longitude)
search_string = 'pharmacy'
distance = miles_to_meter(15)
business_list = []

response = map_client.places_nearby(
    location=location,
    keyword=search_string,
    name='nursing home',
    radius=distance
    )

# print(response.get('results'))
business_list.extend(response.get('results'))
# next_page_token = response.get('next_page_token')

# while next_page_token:
#     time.sleep(2)
#     response = map_client.places_nearby(
#         location=location,
#         keyword=search_string,
#         name='pharmacy',
#         radius=distance,
#         page_token = next_page_token
#     )
#     business_list.extend(response.get('results'))
#     next_page_token = response.get('next_page_token')

df = pd.DataFrame(business_list)
df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
print(df.head())