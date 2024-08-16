import json

def load_files():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)

    except FileNotFoundError:
        return []