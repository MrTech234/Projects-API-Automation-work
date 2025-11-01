import requests
url = "https://wttr.in/agbor? format = j1"
response = requests.get(url)
print(response.text)
data = response.json()
current = data["current_condition"] [0]
temp = current ["temp_c"]
humidity = current ["humidity"]
desc = current ["weather Desc"] [0] ["value"]
print(f"weather in agbor")
print(f"Temprature: {temp} °c")
print(f"Humidity: {humidity} %")
print(f"Condition: {desc}")

