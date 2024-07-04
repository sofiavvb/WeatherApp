import requests
from integracaosheets import *
from datetime import datetime
from functions import saveDataToJson

#Para usar a api do open weather
API_KEY = os.getenv("API_KEY")

def get_weather_info():
    city = input("Choose a city: ")
    lang = "pt_br"
    date = datetime.now()
    date = date.strftime('%Y-%m-%d %H:%M:%S')

    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang={lang}&units=metric"

    #pegar informações da API (get)
    request = requests.get(link)
    #converter para dicionario
    request_dict = request.json()

    weather_cond = request_dict['weather'][0]['description']
    temp = request_dict['main']['temp']
    humidity = request_dict['main']['humidity']
    #append in the sheets
    update_sheet([[city, weather_cond, temp, humidity, date]])
    #transform to json object
    saveDataToJson(city, weather_cond, temp, humidity, date)
    print("--Info added to the sheet!--")