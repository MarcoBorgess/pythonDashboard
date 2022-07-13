import apiRequests
import datetime
import math

def getRaces():
    racesJson = apiRequests.getF1Calendar()
    return racesJson.MRData.RaceTable.Races

def getNextRound(racesList):
    nextRound = 0;
    today = datetime.datetime.utcnow()
    for race in racesList:
        dateTime = race.date + ' ' + race.time
        raceDateTime = datetime.datetime.fromisoformat(dateTime.replace('Z', '.000000'))
        if (today < raceDateTime):
            nextRound = race.round
            return nextRound
        
def formatDateTime(date, time):
    completeDate = date + ' ' + time
    completeDate = datetime.datetime.fromisoformat(completeDate.replace('Z', '.000000'))

    day = completeDate.strftime('%d')
    month = completeDate.strftime('%b')
    auxHour = completeDate.strftime('%H')
    minutes = completeDate.strftime('%M')

    #UTC-3
    hour = str(int(auxHour)-3)

    newDate = f'{day} de {month} às {hour}:{minutes}h'
    
    return newDate
        
def getNextRace():
    racesList = getRaces()
    class Race:
        def __init__(self, name, circuit, url, mainRaceTime, timeUntil):
            self.name = name
            self.circuit = circuit
            self.url = url
            self.mainRaceTime = mainRaceTime
            self.timeUntil = timeUntil
    
    for race in racesList:
        if (race.round == getNextRound(racesList)):
            nextRace = Race(race.raceName, race.Circuit.circuitName, race.url, formatDateTime(race.date, race.time), getTimeUntil(race.date, race.time))
            return nextRace

def getTimeUntil(date, time):
    completeDate = date + ' ' + time
    completeDate = datetime.datetime.fromisoformat(completeDate.replace('Z', '.000000'))
    now = datetime.datetime.utcnow()
    
    distance = completeDate - now

    days = distance.days
    hours = math.floor(distance.seconds / 60 / 60)
    minutes = math.floor((distance.seconds / 60)-(hours * 60))

    dateString = f'{days}d {hours}h {minutes}m'

    return dateString