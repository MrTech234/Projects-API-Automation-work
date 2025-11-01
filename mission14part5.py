import requests
username = input("Enter a GitHub username:")
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
if response.status_code == 200:
	data = response.json()
	print(f"\nHere are {username}'s public repositories:\n")
	for repo in data[:5]:
		print("-", repo["name"])
else:
	print("User not found or error occurred.")

