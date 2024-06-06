import requests

url = "https://us-central1-storied-polymer-421713.cloudfunctions.net/predict"
files = {"file": open("./0cd1ebaf-3975-4749-b625-50b7b0751c36___RS_Erly.B 7508.JPG", "rb")}
response = requests.post(url, files=files)

print(response.text)
