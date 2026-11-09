import requests

URL = 'http://127.0.0.1:8000/api/v1/'

r = requests.post(URL + 'areas/', json={'nome': 'Qualquer coisa'})
print(r.status_code)
requests.delete(URL + f"areas/{r.json()['id']}/")