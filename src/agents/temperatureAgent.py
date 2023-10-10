from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from messages.constants import OPEN_WEATHER_API_KEY
from utils.alert import send_notification
import os
import requests
import json

location = ""
min_temp, max_temp = None,None
mobileNumber = ""

TEMP_SEED = os.getenv("TEMP_SEED", "temperature really secret phrase :)")

agent = Agent(
    name="temperature_adaptor",
    seed=TEMP_SEED
)

fund_agent_if_low(agent.wallet.address())

API_KEY = OPEN_WEATHER_API_KEY

assert API_KEY, "OPEN_WEATHER_MAP_API_KEY environment variable is missing from .env"

def set_details():
    global location
    global min_temp
    global max_temp
    global mobileNumber
    location = input("Enter the location (Default Location is Delhi) : ")
    min_temp = float(input("Enter the minimum temperature in celcius (Default min is 25C) : "))
    while True:
        max_temp = float(input("Enter the maximum temperature in celcius (Default max is 30C) : "))
        if min_temp<=max_temp:
            break
        else:
            print("Please enter max temperature greater than or equal to min temperature")
    mobileNumber = input("Please input a valid mobile number to notify you : ")
    if location == "":
        location = "Delhi"
    if min_temp == None and max_temp == None:
        min_temp = 25
        max_temp = 30
    elif min_temp == None and max_temp != None:
        min_temp = max_temp-1
    elif min_temp != None and max_temp == None:
        max_temp = min_temp+1


def get_temperature(address):
  encoded_address = requests.utils.quote(address)
  api_url = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_address}&appid={API_KEY}"
  response = requests.get(api_url)
  print("Inside get current temperature function")
  return response

@agent.on_interval(period=20.0)
async def check_temperature(ctx: Context):
    global location
    global min_temp
    global mobileNumber
    try:
        response = get_temperature(location)
        if response.status_code != 200:
            print("API RESPONSE STATUS CODE not 200: ", response.json())
            return
        response = json.loads(response.content)
        temperature = response["main"]["temp"]
        temperature = temperature - 273.15
        temperature = round(temperature)
        print("Current Temperature :",temperature)
        if temperature<min_temp or temperature>max_temp:
            print("Temperature is not with threshold")
            if mobileNumber != "":
                send_notification(mobileNumber, temperature)
    except Exception as exc:
       print(exc)

def start():
    set_details()
    agent.run()