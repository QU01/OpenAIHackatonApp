import requests

url = "http://localhost:5000/api/get-transcription"

response = requests.get(url)

print(response.status_code, response.text)

