import apiRequests
import datetime

def getRaces():
    racesJson = apiRequests.getF1Calendar()
    return racesJson.MRData.RaceTable.Races

def getNextRound(racesList):
    nextRound = 0;
    today = datetime.datetime.utcnow()
    for race in racesList:
        raceDateTime = formatDateTime(race.date, race.time)
        if (today < raceDateTime):
            nextRound = race.round
            return nextRound
        
def formatDateTime(date, time):
    dateTime = date + ' ' + time
    dateTime = datetime.datetime.fromisoformat(dateTime.replace('Z', '.000000'))
    return dateTime
        
def getNextRace():
    racesList = getRaces()
    class Race:
        def __init__(self, name, circuit, url, dateTime, country, flag):
            self.name = name
            self.circuit = circuit
            self.url = url
            self.dateTime = dateTime
            self.country = country
            self.flag = flag
    
    for race in racesList:
        if (race.round == getNextRound(racesList)):
            nextRace = Race(race.raceName, race.Circuit.circuitName, race.url, formatDateTime(race.date, race.time), race.Circuit.Location.country, getFlag(race.Circuit.Location.country))
            return nextRace

def getFlag(country):
    code = 'br'
    match(country):
        case 'France':
            code = 'fr'
    
    return 'https://flagicons.lipis.dev/flags/4x3/' + code + '.svg'