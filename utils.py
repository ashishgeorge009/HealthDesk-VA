import re
import pandas as pd

DETAILS = {
    "name":None,  # Name will be saved as None by default
    "email": None, # Email will be saved as None by default
    "doctor": None, # Doctor will be saved as None by default
    "date": None, # Date will be saved as None by default
    "time": None, # Time will be saved as None by default
    "appointment": None # Appointment will be saved as None by default
}

DATABASE = pd.read_excel('Doctor_database.xlsx')

def extract_value(response):
    '''
    Function to parse the <proto.marshal.collections.maps.MapComposite> response object returned by DialogFlow
    Since, couldn't find a method to extract the values from this kind of object the documentation therefore writing custom text_to_parse_func()
    '''
    text_to_parse_func = str(response.query_result) #converting the response to a string
    
    d = dict() # Dictionary to hold the parameters in key value pairs
    key_pattern = "key: \"(.*?)\"" # Starting pattern of each key to be extracted
    value_pattern = "string_value: \"(.*?)\"" # Starting pattern of each value to be extracted

    while text_to_parse_func:
        key = re.search(key_pattern, text_to_parse_func)
        
        if key is None: # If no key is found that we means we have extracted all the attributes, then break
            break
        key = key.group(1) # To extract the string value of the key
        value = re.search(value_pattern, text_to_parse_func).group(1)
        d[key] = value
        text_to_parse_func = text_to_parse_func[text_to_parse_func.find(value)+len(value):]
    
    return d

def extract_type(text):
    value_pattern = "string_value: \"(.*?)\"" # Starting pattern of each value to be extracted
    type = re.search(value_pattern, text).group(1)
    return type

def extract_details(text):
    '''
    Function to extract the details from the text response I sent
    '''
    text = text.split("|")
    response_text = text[0]
    details_text = text[1]    
    DETAILS.update(zip(DETAILS,details_text.split(',')))
    DETAILS['time'] = format_time(DETAILS['time'])
    return response_text,DETAILS

def format_time(time):
    if len(time)>10:
        time = time.split('T')[1]
        time = time.split('-')[0]
    return time



    