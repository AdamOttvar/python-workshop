# Module for making http requests
import requests
# Used for handling JSON structure
import json
# Used for handling time and formatting time
import datetime


# Key and secret are given when a new application is created at 
# https://developer.vasttrafik.se/
key = 'IWjghf_3NZdMf8NRlkU18EJt1o4a'
secret = 'OTNn1ve9CPCnvAkZfHSKD3q8sG4a'

# The URL and how the request should look is specified at
# https://developer.vasttrafik.se/
url = 'https://api.vasttrafik.se:443/token'
payload = {'Content-Type': 'application/x-www-form-urlencoded',
           'grant_type': 'client_credentials',
           'client_id': key,
           'client_secret': secret}
# Use request to post and get response
response_json = requests.post(url, payload).json()

# An access token is returned, together with when it expires etc
print(response_json)
token = response_json['access_token']
print(token)

# The token can then be used to retrieve data from the API
# For example for a depature board. The documentation is available at
# https://developer.vasttrafik.se/
# In order to get departures you need to get the ID of the stop
elisedal_id = "9021014002210000"
korsvagen_id = "9021014003980000"
# Get current time on the right format
now_time = datetime.datetime.now()
tram_date = now_time.strftime('%Y-%m-%d')
tram_time = now_time.strftime('%H:%M')
url = 'https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard'
payload = {'id': elisedal_id,
        'date': tram_date,
       'time': tram_time,
       'timeSpan': '30',
       'maxDeparturesPerLine': '3',
       'needJourneyDetail': '0',
       'direction': korsvagen_id,
       'format': 'json',}
header = {'Authorization': 'Bearer ' + token}
# Get request
response = requests.get(url = url, headers = header, params = payload).json()
print(json.dumps(response, indent=2))

##################
## Test yourself
##################
# Create a script that prints the next 4 departures from
# Korsvägen 9021014003980000
# to
# Brunnsparken 9021014001760000
# Display their Number, Destination and in how many minutes they
# will departure
