import requests
import time
while True:
	city = "Agbor"
	url = f"https://wttr.in/{city}? format =j1"
	response = requests.get(url)
	print(response.text)
	temp = data["current_condition"] [0] ["temp_c"]
	wind = data["current_condition"] [0] ["windspeed kmph"]
	desc = data["current_condition"] [0] ["weatherDesc"] [0] ["value"]
	print(f"\n weather in {city}")
	print(f"condition: {desc}")
	print(f"Temperature: {temp} °c")
	print(f"wind speed: {wind} km/h")
	print("Refreshing again in 10 seconds...\n")
	time.sleep(10)

