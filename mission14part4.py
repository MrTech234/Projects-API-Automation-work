import requests
response = requests.get("https://api.github.com/repositories")
data = response.json()
print("\n Here are the names of 5 public GitHub repositories:\n")
for repo in data[:5]:
	print("-", repo["name"])
