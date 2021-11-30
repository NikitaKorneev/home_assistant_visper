import os
import requests
import json
from requests import auth
from requests.auth import HTTPBasicAuth

with open("./secrets.json","r") as cred:
    creds = cred.read()
    creds2 = json.loads(creds)
    un = creds2["credentials"]["username"]
    pw = creds2["credentials"]["password"]


texts = [
    "Здорова, ватное быдло! Как дела? Ну что, можно тебя поздравить! Ты did it",
    "Лох! Пидр, нет друзей!",
]

token = requests.post("https://visper.tech/api/token/", {
    "username":un,
    "password":pw
}
)

head = token.json()["access"]

dat = {
    "name": "Новый ролик",
    "speaker_id": 324,
    "ttl": 0,
    "sections": [
        {
            "text": texts[0],
            "avatar_position": "upToChest",
            "avatar_align": "center",
            "avatar_scale": 100,
            "content_scale": 100,
            "viewed": True,
        }
    ]
}
content_upload = requests.get(
    "https://visper.tech/api/document/",
    data={
    "name": "Новый ролик",
    "speaker_id": 324,
    "ttl": 0,
    "sections": [
        {
            "text": texts[0],
            "avatar_position": "upToChest",
            "avatar_align": "center",
            "avatar_scale": 100,
            "content_scale": 100,
            "viewed": True,
        }
    ]
},
    headers={"Authorization": "Bearer " + head},
)

#print(token.json()["access"])
#print(content_upload.json())
fileMF = requests.get("https://visper.tech/api/document/start/127027",
headers={"Authorization": "Bearer " + head},
)
#print(fileMF.json())
print(os.getcwd())
print(un, pw)