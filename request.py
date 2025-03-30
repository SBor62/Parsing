import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {'userId': 1}

response = requests.get(url, params=params)

if response.status_code == 200:
    # Парсим JSON-ответ
    posts = response.json()

    for post in posts:
        print(post)
else:
    print(f"Ошибка: {response.status_code}")