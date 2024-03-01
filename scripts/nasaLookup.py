import requests

astros = requests.get("http://api.open-notify.org/astros.json")
print(astros.json()["people"])
