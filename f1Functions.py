import apiRequests
import datetime

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
        def __init__(self, name, circuit, url, mainRaceTime):
            self.name = name
            self.circuit = circuit
            self.url = url
            self.mainRaceTime = mainRaceTime
    
    for race in racesList:
        if (race.round == getNextRound(racesList)):
            nextRace = Race(race.raceName, race.Circuit.circuitName, race.url, formatDateTime(race.date, race.time))
            return nextRace
