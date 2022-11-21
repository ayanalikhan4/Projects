import requests
from datetime import *
import smtplib
import time


MY_EMAIL = "ali9968069546@gmail.com"
MY_PASSWORD = "test"
MY_LAT = 43.452969
MY_LNG = -80.495064

def is_iss_overhead():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LNG-5<=iss_longitude<=MY_LNG+5:
        return True

def is_night():

    parameters = {
        "lat":MY_LAT,
        "lang":MY_LNG,
        "formatted":0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1][:2])
    sunset = int(data["results"]["sunset"].split("T")[1][:2])

    time_now = datetime.now().hour()

    if time_now>=sunset or time_now<=sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg= "Subject:Look Up\n\n The ISS is above you in the sky"
        )



