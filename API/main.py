import requests

MY_LAT = 43.452969

MY_LNG = -80.495064


"""
response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

print(data)
"""

parameters = {
    "lat":MY_LAT,
    "lang":MY_LNG,

}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()

data = response.json()
print(data)
