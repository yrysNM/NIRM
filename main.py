import requests; 

url = 'https://cvparser.ai/api/v4/parse'
headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'f7e4d3c3cb17cea1b1d0362fb45685b6'
}
data = {
    'url': 'https://docs.google.com/document/d/1MWylZf0vpDkR0mQ7L2XRmA0yCptrUTcY6klINukWd6w/export?format=pdf'
}

response = requests.post(url, headers=headers, json=data)
print(response.json())