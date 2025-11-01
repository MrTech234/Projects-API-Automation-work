import requests

# Replace with your city coordinates (Agbor: latitude=6.26, longitude=6.18)
url = "https://api.open-meteo.com/v1/forecast?latitude=6.26&longitude=6.18&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current = data["current_weather"]
    temp = current["temperature"]
    wind = current["windspeed"]
    print("🌤 Weather in Agbor")
    print(f"Temperature: {temp}°C")
    print(f"Wind Speed: {wind} km/h")
else:
    print("❌ Failed to fetch weather data. Status:", response.status_code)
