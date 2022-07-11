import requests
import json
from types import SimpleNamespace

def getF1Calendar():

    result = requests.get('http://ergast.com/api/f1/current.json')
    data = json.loads(result.text, object_hook=lambda d: SimpleNamespace(**d))
    
    return data;