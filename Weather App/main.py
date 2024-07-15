import requests
import json

city=input("Enter the City name: ")

api_key="e1d983b04e077c29b80e04718e8ac714"

url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

r=requests.get(url)

wdata=r.json()
if "main" in wdata:
    temp_k = wdata['main']['temp']
    temp_c = temp_k - 273.15
    print(f"Current temperature in {city} is {temp_c:.2f}° C")
else:
    raise Exception("Enter valid City name")