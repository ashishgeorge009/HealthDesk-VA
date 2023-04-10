import googlemaps
import pandas as pd
import time
from geopy.geocoders import Nominatim
import warnings

"""
FUTURE WORK TO IMPLEMENT THIS
"""

def miles_to_meter(miles):
    try:
        return miles * 1609.344
    except:
        return 0

def get_nearby(type_ ):
    '''Function to find the nearby locations of anything given in the search term'''
    location = input("Enter text: ")

    API_KEY = open('API_KEY.txt','r').read()
    map_client = googlemaps.Client(API_KEY)

    geolocator = Nominatim(user_agent="receptionist")
    location = geolocator.geocode(location)             # Getting the location in terms of latitude and longitude

    location = (location.latitude, location.longitude)      
    search_string = type_
    distance = miles_to_meter(15)
    business_list = []                                  # List to store all the results

    response = map_client.places_nearby(
        location=location,
        keyword=search_string,
        name=type_,
        radius=distance
    )
    business_list.extend(response.get('results'))       # Adding the results to the list
    df = pd.DataFrame(business_list)
    df['Open Now'] = df['opening_hours'].apply(pd.Series)['open_now']       # One of the columns was a dict, so this line converts it to a separate column and appends it to the dataframe
    data = df[['name','Open Now','rating']]          # Extracting only the relevant data
    
    # Renaming True and False to Open Now and Closed
    data.loc[data['Open Now']==True,['Open Now']] = "Open"
    data.loc[data['Open Now']==False,['Open Now']] = "Closed"

    warnings.filterwarnings("ignore")
    data.rename(columns={'name':'Name','rating':'Rating'},inplace=True)
    pd.set_option('display.max_columns', None)
    print("\n")
    print(data.head())
    print("\n")

    return f"Here are the {type_} near you, let me know if you need anything else. Bye"

