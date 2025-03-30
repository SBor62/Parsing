import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post(url, json=data)

print(f"Status_code: {response.status_code}")
print(f"Содержимое ответа: {response.json()}")
