import requests

api_key = "75f99c6e5bf613675e743a9c3ab32009"
cityName = "Taipei"

def get_forecast_data():
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cityName},tw&APPID={api_key}&lang=zh_tw&units=metric"

    response = requests.get(url=url)

    if response.ok:
        print("下載成功")
        print(response.text)
    else:
        print("下載失敗")