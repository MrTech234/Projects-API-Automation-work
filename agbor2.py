import requests

url = "https://wttr.in/Agbor?format=j1"
response = requests.get(url)

try:
    data = response.json()
    print("✅ JSON received!")
    print(data["current_condition"][0]["temp_C"])
except ValueError:
    print("⚠️ Not JSON, here’s the raw text:")
    print(response.text)
