import requests


def get_weather(city):

    try:
        # Step 1: Get city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return {"error": "City not found. Please enter a valid city name."}

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Step 2: Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "precipitation",
                "weather_code"
            ],
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]

        return {
            "city": location["name"],
            "country": location.get("country", ""),
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "rainfall": current["precipitation"],
            "weather_code": current["weather_code"],
            "time": current["time"]
        }

    except requests.RequestException:
        return {"error": "Unable to connect to weather service. Please try again."}

    except (KeyError, IndexError, ValueError):
        return {"error": "Weather information is currently unavailable."}
    
def get_farming_advice(weather):

    code = weather["weather_code"]
    temperature = weather["temperature"]
    humidity = weather["humidity"]
    rainfall = weather["rainfall"]

    # Weather condition
    if code == 0:
        condition = "Clear Sky"
    elif code in [1, 2, 3]:
        condition = "Partly Cloudy"
    elif code in [45, 48]:
        condition = "Foggy"
    elif code in [51, 53, 55, 56, 57]:
        condition = "Drizzle"
    elif code in [61, 63, 65, 66, 67, 80, 81, 82]:
        condition = "Rainy"
    elif code in [71, 73, 75, 77, 85, 86]:
        condition = "Snowy"
    elif code in [95, 96, 99]:
        condition = "Thunderstorm"
    else:
        condition = "Unknown Weather"

    # Farming recommendations
    advice = []

    if temperature >= 35:
        advice.append(
            "High temperature: Monitor crops for heat stress and irrigate appropriately."
        )
    elif temperature <= 10:
        advice.append(
            "Low temperature: Monitor crops for cold stress and protect sensitive plants."
        )
    else:
        advice.append(
            "Temperature is moderate. Continue regular crop monitoring."
        )

    if humidity >= 80:
        advice.append(
            "High humidity: Improve air circulation and monitor crops for fungal diseases."
        )

    if rainfall > 0:
        advice.append(
            "Rainfall detected: Check field drainage and avoid unnecessary irrigation."
        )
    else:
        advice.append(
            "No current precipitation: Check soil moisture before irrigation."
        )

    return {
        "condition": condition,
        "advice": advice
    }