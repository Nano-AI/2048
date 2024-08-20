import json

def get_settings():
    f = open("settings.json")
    data = json.load(f)
    f.close()
    return data
