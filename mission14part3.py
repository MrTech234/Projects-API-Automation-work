import requests
response = requests.get("https://api.github.com")
data = response.json()
print("The value of 'current_user_url' is:")
print(data["current_user_url"])
print("\n Another one Motherfucker:")
print(data["commit_search_url"])

