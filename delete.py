import database, get
from geopy.distance import geodesic
import json
import requests

def userInterest(id, interestId):
    sql = 'DELETE FROM userInterests WHERE userId = '+str(id)+' AND interestId = '+str(interestId)
    database.sendToServer(sql)

def allUserInterest(id):
    sql = 'DELETE FROM userInterests WHERE userId = '+str(id)
    database.sendToServer(sql)

def userInterestFilter(id, interestId):
    sql = 'DELETE FROM userInterestsFilter WHERE userId = '+str(id)+' AND interestId = '+str(interestId)
    database.sendToServer(sql)

def allUserInterestFilter(id):
    sql = 'DELETE FROM userInterestsFilter WHERE userId = '+str(id)
    database.sendToServer(sql)

def userGenderFilter(id, genderId):
    sql = 'DELETE FROM userGendersFilter WHERE userId = '+str(id)+' AND genderId = '+str(genderId)
    database.sendToServer(sql)

def allUserGenderFilter(id):
    sql = 'DELETE FROM userGendersFilter WHERE userId = '+str(id)
    database.sendToServer(sql)

def userAgeFilter(id):
    sql = 'DELETE FROM userAgeFilter WHERE userId = '+str(id)
    database.sendToServer(sql)

def userDistanceFilter(id):
    sql = 'DELETE FROM userDistanceFilter WHERE userId = '+str(id)
    database.sendToServer(sql)

def allUserActions(id):
    sql = 'DELETE FROM userActions WHERE firstUserId = ' + str(id) + ' OR secondUserId = '+  str(id)
    database.sendToServer(sql)

def usersActions():
    sql = 'DELETE FROM userActions WHERE isLike = 0'
    database.sendToServer(sql)

def user(id):
    allUserInterest(id)
    allUserInterestFilter(id)
    allUserGenderFilter(id)
    userAgeFilter(id)
    userDistanceFilter(id)
    allUserActions(id)
    sql = 'DELETE FROM users WHERE id = '+str(id)
    database.sendToServer(sql)

