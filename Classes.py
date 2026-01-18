import json

with open("./front/data.json") as f:
    base = json.load(f)[0]

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    