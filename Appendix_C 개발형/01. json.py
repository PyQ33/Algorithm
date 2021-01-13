import requests

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

data = response.json()

print(data)

name_list = []
for unit in data:
    name_list.append(unit['name'])

print(name_list)