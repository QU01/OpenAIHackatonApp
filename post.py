import requests

url = "http://localhost:5000/api/upload-audio"

audio_file = open("audio.wav", "rb")

files = {"audio": audio_file}

response = requests.post(url, files=files)

print(response.status_code, response.text)