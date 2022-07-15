from encodings.utf_8 import encode
import requests
import json
import os
from types import SimpleNamespace


def getF1Calendar():
    try:
        with open('apiResults/f1Calendar.json', encoding='utf-8') as jsonFile:
            data = json.load(jsonFile, object_hook=lambda d: SimpleNamespace(**d))
        return data
    except:
        result = requests.get('http://ergast.com/api/f1/current.json')
        data = result.content
        with open('apiResults/f1Calendar.json', 'wb') as f:
            f.write(data)
        cbData = json.loads(result.text, object_hook=lambda d: SimpleNamespace(**d))
        print('CALENDAR UPDATED FROM API')
        return cbData

def updateF1Calendar():
    if os.path.exists("apiResults/f1Calendar.json"):
        os.remove("f1Calendar.json")
        try:
            getF1Calendar()
            return("Updated")
        except:
            return("Couldnt Update")
    else:
        return("The file does not exist")