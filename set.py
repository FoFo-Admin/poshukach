import database, get
from geopy.distance import geodesic
import json
import requests

#INSERTS
def createUser(id):
    sql = 'INSERT INTO users (id, activity) VALUES (' + str(id) + ', 0)'
    database.sendToServer(sql)

def createCity(response):
    sql = ('INSERT INTO cities (fullTitle, showTitle, latitude, longitude) VALUES ("'+response.json()['results'][0]['formatted']
            +'", "' + response.json()['results'][0]['formatted'].split(",")[0]
            +'", ' + str(response.json()['results'][0]['geometry']['lat'])
            + ', '+str(response.json()['results'][0]['geometry']['lng'])+')')
    database.sendToServer(sql)

def userInterest(id, interestId):
    sql = 'INSERT INTO userInterests (userId, interestId) VALUES ('+str(id)+', '+str(interestId)+')'
    database.sendToServer(sql)

def userAgeFilter(id, minAge, maxAge):
    sql = 'INSERT INTO userAgeFilter (userId, minAge, maxAge) VALUES ('+str(id)+', '+str(minAge)+', '+str(maxAge)+')'
    database.sendToServer(sql)

def userDistanceFilter(id, maxdistance):
    sql = 'INSERT INTO userDistanceFilter (userId, maxDistance) VALUES ('+str(id)+', '+str(maxdistance)+')'
    database.sendToServer(sql)

def userInterestFilter(id, interestId):
    sql = 'INSERT INTO userInterestsFilter (userId, interestId) VALUES ('+str(id)+', '+str(interestId)+')'
    database.sendToServer(sql)

def userGenderFilter(id, genderId):
    sql = 'INSERT INTO userGendersFilter (userId, genderId) VALUES ('+str(id)+', '+str(genderId)+')'
    database.sendToServer(sql)

def likeordislike(firstId, secondId, isLike):
    sql = 'INSERT INTO userActions (firstUserId, secondUserId, isLike) VALUES ('+str(firstId)+', '+str(secondId)+', '+str(isLike)+')'
    database.sendToServer(sql)



#UPDATES
def changeLikeToFalse(firstId, secondId):
    sql = 'UPDATE userActions SET isLike = 0 WHERE firstUserId = '+str(secondId)+' AND secondUserId = '+str(firstId)
    database.sendToServer(sql)

def userState(id, newState):
    sql = ('UPDATE users SET userState="'+newState+'" WHERE id = '+str(id))
    database.sendToServer(sql)

def username(id, username):
    sql = ('UPDATE users SET username="'+username+'" WHERE id = '+str(id))
    database.sendToServer(sql)

def usernameNULL(id):
    sql = ('UPDATE users SET username=NULL WHERE id = '+str(id))
    database.sendToServer(sql)

def name(id, name):
    sql = ('UPDATE users SET name="'+name+'" WHERE id = '+str(id))
    database.sendToServer(sql)

def description(id, description):
    sql = ('UPDATE users SET description="'+description+'" WHERE id = '+str(id))
    database.sendToServer(sql)

def age(id, age):
    sql = ('UPDATE users SET age='+str(age)+' WHERE id = '+str(id))
    database.sendToServer(sql)

def genderId(id, genderId):
    sql = ('UPDATE users SET genderId='+genderId+' WHERE id = '+str(id))
    database.sendToServer(sql)

def purposeId(id, purposeId):
    sql = ('UPDATE users SET purposeId='+purposeId+' WHERE id = '+str(id))
    database.sendToServer(sql)

def clientLanguageId(id, languageId):
    sql = ('UPDATE users SET clientLanguageId="'+languageId+'" WHERE id = '+str(id))
    database.sendToServer(sql)

def imageAdded(id, bit):
    sql = ('UPDATE users SET imageAdded='+bit+' WHERE id = '+str(id))
    return database.sendToServer(sql)

def cityId(id, response):
    if not get.isCityExists(response.json()['results'][0]['formatted']): 
        createCity(response)
        cityId(id, response)
    else:
        sql = ('UPDATE users SET cityId='+str(get.cityByFullTitle(response.json()['results'][0]['formatted']))+' WHERE id = '+str(id))
        database.sendToServer(sql)

def userMinAgeFilter(id, minAge):
    sql = 'UPDATE userAgeFilter SET minAge='+str(minAge)+' WHERE userId='+str(id)
    database.sendToServer(sql)

def userMaxAgeFilter(id, maxAge):
    sql = 'UPDATE userAgeFilter SET maxAge='+str(maxAge)+' WHERE userId='+str(id)
    database.sendToServer(sql)

def userMaxDistanceFilter(id, maxDistance):
    sql = 'UPDATE userDistanceFilter SET maxDistance='+str(maxDistance)+' WHERE userId='+str(id)
    database.sendToServer(sql)

def plusUserActivity(id):
    sql = 'UPDATE users SET activity = activity+1 WHERE id = '+str(id)
    database.sendToServer(sql)

def updateAllUsersActivity():
    sql = 'UPDATE users SET activity = activity/2'
    database.sendToServer(sql)
