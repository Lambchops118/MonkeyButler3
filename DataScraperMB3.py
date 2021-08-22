
#Monkey Butler Data Scraper Module
#Part of Monkey Butler 3

import requests
import cryptocompare
from astral import moon
import time
import datetime


def temperature():
    key = "c5bbe0c6b2d7ab5f9ae92a9441d47253"
    urlBase = "http://api.openweathermap.org/data/2.5/weather?"
    nameCity = "Chadds Ford"
    urlComplete = urlBase + "appid=" + key + "&q=" + nameCity
    response = requests.get(urlComplete)
    x= response.json()

    if x["cod"] != "404":
            y = x["main"]
            current_temp = y["temp"]
            current_pres = y["pressure"]
            current_hum = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
    else:
        print("I cannot find that city.")

    temp = round(current_temp * 9/5-459.67)
    return temp

def humidity():
    key = "c5bbe0c6b2d7ab5f9ae92a9441d47253"
    urlBase = "http://api.openweathermap.org/data/2.5/weather?"
    nameCity = "Chadds Ford"
    urlComplete = urlBase + "appid=" + key + "&q=" + nameCity
    response = requests.get(urlComplete)
    x= response.json()
    if x["cod"] != "404":
            y = x["main"]
            current_temp = y["temp"]
            current_pres = y["pressure"]
            current_hum = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
    else:
        print("I cannot find that city.")

    humidity = current_hum
    return humidity

#Astronomy
year = int(time.strftime("%Y"))
month = int(time.strftime("%m"))
day = int(time.strftime("%d"))

def moonPhase():
    phase = moon.phase(datetime.date(year, month, day))
    if phase <= 6.99:
        x = "New Moon"
        return x
    elif phase <= 13.99:
        x = "First Quarter"
        return x
    elif phase <= 20.99:
        x = "Full Moon"
        return x
    elif phase <= 27.99:
        x = "Last Quarter"
        return x
    else:
        return "Error."

def moonInt():
    phaseInt = round(moon.phase(datetime.date(year, month, day)), 2)
    return phaseInt


#Cryptocurrency
def bitcoinPrice():
    p = str(cryptocompare.get_price('BTC',currency='USD',full=False))
    x = p.replace("{", "").replace("BTC", "").replace("USD", "").replace(":", "").replace("'", "").replace('}}', "").replace(" ", "")
    return x
def ethereumPrice():
    p = str(cryptocompare.get_price('ETH',currency='USD',full=False))
    x = p.replace("{", "").replace("ETH", "").replace("USD", "").replace(":", "").replace("'", "").replace('}}', "").replace(" ", "")
    return x
def litecoinPrice():
    p = str(cryptocompare.get_price('LTC',currency='USD',full=False))
    x = p.replace("{", "").replace("LTC", "").replace("USD", "").replace(":", "").replace("'", "").replace('}}', "").replace(" ", "")
    return x
def zcashPrice():
    p = str(cryptocompare.get_price('ZEC',currency='USD',full=False))
    x = p.replace("{", "").replace("ZEC", "").replace("USD", "").replace(":", "").replace("'", "").replace('}}', "").replace(" ", "")
    return x
def chainlinkPrice():
    p = str(cryptocompare.get_price('LINK',currency='USD',full=False))
    x = p.replace("{", "").replace("LINK", "").replace("USD", "").replace(":", "").replace("'", "").replace('}}', "").replace(" ", "")
    return x

