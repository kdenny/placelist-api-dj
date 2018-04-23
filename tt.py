import requests

data = {'username': 'deez', 'password': 'password'}
rf = requests.post('http://localhost:8000/auth/obtain_token/', data=data)
print(rf.text)