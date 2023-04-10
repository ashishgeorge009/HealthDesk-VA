import os
import json
from google.cloud import dialogflow
from google.api_core.exceptions import InvalidArgument

## The private_key json is saved separately after downloading from the Diagflow
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

DIALOGFLOW_PROJECT_ID = 'health2.0'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

def get_response(text_to_be_analyzed):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    
    return response

