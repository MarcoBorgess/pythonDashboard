from asyncio.windows_events import NULL
import controller.f1Requests as f1Requests
import datetime
import math

def getRaces():
    racesJson = f1Requests.getF1Calendar()
    return racesJson.MRData.RaceTable.Races
        
def getNextRace():    
    class Race:
        def __init__(self, name, url, round, time, date):
            self.name = name
            self.url = url
            self.round = round
            self.time = time
            self.date = date
            self.events = []
        
        def addEvent(self, event):
            self.events.append(event)

        def getDateTime(self):
            return getDateTimeType(self.date, self.time)

        def getFormatedDateTime(self):
            return formatDateTime(self.date, self.time)
        
        def getTimeUntil(self):
            return getTimeUntil(self.date, self.time)

        def getDayOfWeek(self):
            return getDateTimeType(self.date, self.time).strftime('%a').capitalize()
        
    class Event:
        def __init__(self, name, date, time):
            self.name = name
            self.time = time
            self.date = date

        def getDateTime(self):
            return getDateTimeType(self.date, self.time)
            
        def getFormatedDateTime(self):
            return formatDateTime(self.date, self.time)
        
        def getTimeUntil(self):
            return getTimeUntil(self.date, self.time)

        def getDayOfWeek(self):
            return getDateTimeType(self.date, self.time).strftime('%a').capitalize()
    
    raceList = getRaces()
    
    for r in raceList:
        if (r.round == getNextRound(raceList)):
            race = Race(r.raceName,
                        r.url,
                        r.round,
                        r.time,
                        r.date
                    )
            
            p1 = Event('First Practice', r.FirstPractice.date, r.FirstPractice.time)
            p2 = Event('Second Practice', r.SecondPractice.date, r.SecondPractice.time)
            qualy = Event('Qualifying', r.Qualifying.date, r.Qualifying.time)
            mainRace = Event('Race', r.date, r.time)

            if hasattr(r, 'ThirdPractice'):
                p3 = Event('Third Practice', r.ThirdPractice.date, r.ThirdPractice.time)
                race.addEvent(p3)
            elif hasattr(r, 'Sprint'):
                sprint = Event('Sprint', r.Sprint.date, r.Sprint.time)
                race.addEvent(sprint)

            race.addEvent(p1)
            race.addEvent(p2)
            race.addEvent(qualy)
            race.addEvent(mainRace)
            race.events.sort(key=lambda event: event.getDateTime())

            return race

def getAfterRaces():
    class Race:
        def __init__(self, name, round, time, date, circuitName):
            self.name = name
            self.round = round
            self.time = time
            self.date = date
            self.circuitName = circuitName
            
        def __repr__(self) -> str:
            return f'{self.name} - {self.circuitName}'

        def getDateTime(self):
            return getDateTimeType(self.date, self.time)

        def getFormatedDateTime(self):
            return formatDateTime(self.date, self.time)
        
        def getTimeUntil(self):
            return getTimeUntil(self.date, self.time)

        def getDay(self):
            return getDateTimeType(self.date, self.time).day

        def getMonth(self):
            return getDateTimeType(self.date, self.time).strftime('%b').capitalize()
    
    racesList = getRaces()
    afterRaces = []

    for r in racesList:
        if (int(r.round) > int(getNextRound(racesList))):
            afterRaces.append(Race(r.raceName, r.round, r.time, r.date, r.Circuit.circuitName))
    
    return afterRaces
            
def getNextRound(raceList):
    nextRound = 0;
    today = datetime.datetime.utcnow()
    for race in raceList:
        completeDate = getDateTimeType(race.date, race.time)
        if (today < completeDate):
            nextRound = race.round
            return nextRound

def getDateTimeType(date, time):
    completeDate = date + ' ' + time
    completeDate = datetime.datetime.fromisoformat(completeDate.replace('Z', '.000000'))

    return completeDate

def formatDateTime(date, time):
    completeDate = getDateTimeType(date, time)

    day = completeDate.strftime('%d')
    month = completeDate.strftime('%b')
    auxHour = completeDate.strftime('%H')
    minutes = completeDate.strftime('%M')

    #UTC-3
    hour = str(int(auxHour)-3)

    newDate = f'{day} de {month} - {hour}:{minutes}h'
    
    return newDate

def getTimeUntil(date, time):
    completeDate = getDateTimeType(date, time)
    now = datetime.datetime.utcnow()
    
    distance = completeDate - now

    days = distance.days
    hours = math.floor(distance.seconds / 60 / 60)
    minutes = math.floor((distance.seconds / 60)-(hours * 60))

    dateString = f'{days}d {hours}h {minutes}m'

    return dateString

def getDriverStandings():
    driverStanding = f1Requests.getDriverStanding()
    driverStanding = driverStanding.MRData.StandingsTable.StandingsLists[0].DriverStandings
    
    drivers = []
             
    for driver in driverStanding:
        drivers.append(
            {
                "Driver": f'{driver.Driver.givenName} {driver.Driver.familyName}',
                "Points": driver.points,
                "Wins": driver.wins,
                "Position": driver.position,
                "Constructor": driver.Constructors[0].name,
                "Nationality": driver.Driver.nationality
            }
        )
        
    return drivers