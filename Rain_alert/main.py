import requests
api_key = "67ac483a0d96cdc285a3abc5a4c010e0"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

MY_LAT = 43.452969
MY_LNG = -80.495064

parameters = {
        "lat":MY_LAT,
        "lang":MY_LNG,
        "appid": api_key
}

    

response = requests.get(OWM_Endpoint,params = parameters)
response.raise_for_status()