import json
import uuid

with open("./front/data.json") as f:
    base = json.load(f)[0]

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def add_db(self):
        uid = str(uuid.uuid4())[:7]
        key = f"user - #{uid}"
        base[key] = {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }