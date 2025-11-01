import requests
response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
data = response.json()
print("\n Here are the first few keys returned by the API:")
for key in list(data.keys())[:5]:
	print("-", key)
