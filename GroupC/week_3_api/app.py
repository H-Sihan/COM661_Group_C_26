import requests

api_key = ""

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid':api_key, 'units':'metric'}
    response = requests.get(base_url, params=params)
     
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temp: {data['main']['temp']} c")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("city not found")
        
        
city = input("Enter city name: ")
get_weather(city)
    
    
