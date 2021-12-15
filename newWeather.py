import requests

def get_weather_desc_and_temp():
    api_key = "028f5def1f8f34cb96c3c9597157394a"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    requests = requests.get(url)
    json = requests.json()

    description = json.get("weather")[0].get("discription")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return{'description': description,
           'temp_min': temp_min,
           'temp_max': temp_max}

def main():
# Print the results
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is", weather_dict.get(description))
    print("the minimum temperature is", weather_dict.get(temp_min))
    print("the maximum temperature is", weather_dict.get(temp_max))

main()