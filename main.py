import os
import requests
from dotenv import load_dotenv
import pprint

load_dotenv(override=True)
api_key = os.getenv("api_key_weather")
link_api = "http://api.weatherapi.com/v1/current.json"

parameter = {
    "key": api_key,
    "q": "São Paulo",
    "lang": "pt"
}

response_api = requests.get(link_api, params=parameter)

if response_api.status_code == 200:
    request_data = response_api.json()
    # All json printed: pprint.pprint(request_data)
    temp = request_data["current"]["temp_c"]
    climate = request_data["current"]["condition"]["text"]
    print(f"A temperatura de {parameter["q"]} é de {temp}°C no momento. E o clima está {climate}!")
else:
    print(f"Falha na requisição. Código de status: {response_api.status_code}")