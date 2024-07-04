import json
import pandas as pd

def saveDataToJson(city: str, weather_cond: str, temp: float, humidity: float, date: str) -> None:
    #auxiliar dict
    data = {
        'city': city,
        'weather condition': weather_cond,
        'temperature': temp,
        'humidity': humidity,
        'date': date,
    }

    try:
        with open("data.json", 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Couldn't read file")
        existing_data = []

    existing_data.append(data)

    with open("data.json", 'w') as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)

def showDataFrame(city: str, weather_cond: str, temp: float, humidity: float, date: str):
    data = {
        'City': [city],
        'Weather condition': [weather_cond],
        'Temperature(°C)': [temp],
        'Humidity(%)': [humidity],
        'Date': [date],
    }
    data_df = pd.DataFrame(data)
    print(data_df)