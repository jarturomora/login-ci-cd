import json

def load_users():
    with open("users.json") as f:
        return json.load(f)

def login(username, password):
    users = load_users()
    return users.get(username) == password
