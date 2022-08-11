import requests
import requests_cache
import json
from datetime import timedelta
from types import SimpleNamespace

requests_cache.install_cache('f1_cache', backend='sqlite', expire_after=timedelta(hours=6))

def getF1Calendar():
    result = requests.get('https://ergast.com/api/f1/current.json')
    data = json.loads(result.text, object_hook=lambda d: SimpleNamespace(**d))
    return data
    
def getDriverStanding():
    result = requests.get('https://ergast.com/api/f1/2022/driverStandings.json')
    data = json.loads(result.text, object_hook=lambda d: SimpleNamespace(**d))
    return data
    
def getConstructorStanding():
    result = requests.get('https://ergast.com/api/f1/2022/constructorStandings.json')
    data = json.loads(result.text, object_hook=lambda d: SimpleNamespace(**d))
    return data

def updateF1():
    requests_cache.clear()
    return 'F1 cache updated'