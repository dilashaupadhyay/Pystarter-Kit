import requests

# Get your API key by signing up at https://openweathermap.org/,
# creating an account, and generating the API key in the API keys section.
# Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key.

def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name},NP&appid={api_key}"  # Append ",NP" to specify Nepal
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_description = data["weather"][0]["description"]
        return {
            "Temperature": temperature,
            "Humidity": humidity,
            "Description": weather_description
        }
    else:
        return None

def main():
    city_name = input("Enter the city name in Nepal: ")
    api_key = "17ffe84828c6e402782f34e285fb4f1f"  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    weather_data = get_weather_data(city_name, api_key)
    if weather_data:
        print(f"Weather in {city_name}, Nepal:")
        print(f"Temperature: {weather_data['Temperature']} Kelvin")
        print(f"Humidity: {weather_data['Humidity']} %")
        print(f"Weather Description: {weather_data['Description']}")
    else:
        print(f"Weather data not found for {city_name}.")

if __name__ == '__main__':
    main()
