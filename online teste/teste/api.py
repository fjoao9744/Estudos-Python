import requests

url = "http://192.168.15.7:8000/teste.json"

resp = requests.get(url)

print(resp.json())