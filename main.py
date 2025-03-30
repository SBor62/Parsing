import requests

url = "https://api.github.com/search/repositories"

params = {"q": "Language:html"}

respons = requests.get(url, params=params)

print(f"Status code: {respons.status_code}")
print(respons.json())
