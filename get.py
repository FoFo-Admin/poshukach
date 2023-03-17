import database

#users
def isAccountExist(id):
    sql = 'SELECT * FROM users WHERE id = '+ str(id)
    if not database.getFromServer(sql):
        return False
    return True

def state(id):
    sql = 'SELECT userState FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def username(id):
    sql = 'SELECT username FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def name(id):
    sql = 'SELECT name FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def description(id):
    sql = 'SELECT description FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def age(id):
    sql = 'SELECT age FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def genderId(id):
    sql = 'SELECT genderId FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def cityId(id):
    sql = 'SELECT cityId FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def purposeId(id):
    sql = 'SELECT purposeId FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def clientLanguage(id):
    sql = 'SELECT clientLanguageId FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def imageAdded(id):
    sql = 'SELECT imageAdded FROM users WHERE id = '+ str(id)
    return database.getFromServer(sql)[0][0]

def userInfo(id):
    language = clientLanguage(id)
    purpose = ''

    if language=="Ukrainian":
        purpose='UA'
    elif language=="Russian":
        purpose='RU'
    elif language=="English":
        purpose='EN'

    sql = ('SELECT u.name, u.description, u.age, c.showTitle, p.'+purpose+' '
    + 'FROM users u '
    + 'INNER JOIN cities c ON u.cityId = c.id '
    + 'INNER JOIN purposes p ON u.purposeId = p.id '
    + 'WHERE u.id = '+ str(id))
    return database.getFromServer(sql)[0]

#userInterests
def isUserInterestsExist(id):
    sql = 'SELECT userId, interestId FROM userInterests where userId = '+ str(id) 
    if not database.getFromServer(sql):
        return False
    return True

def userInterests(id):
    sql = 'SELECT userId, interestId FROM userInterests where userId = '+ str(id)
    return database.getFromServer(sql)

def userInterestsWords(id):
    language = clientLanguage(id)
    interest = ''

    if language=="Ukrainian":
        interest='UA'
    elif language=="Russian":
        interest='RU'
    elif language=="English":
        interest='EN'

    sql = ('SELECT i.'+interest+' FROM userInterests u '+
    'INNER JOIN interests i ON i.id = u.interestId '
    +' WHERE u.userId = '+ str(id))
    return database.getFromServer(sql)

def countUserInterests(id):
    sql = 'SELECT COUNT(*) FROM userInterests where userId = '+ str(id)
    return database.getFromServer(sql)[0][0]

#languages
def languagesList():
    sql = 'SELECT languageCode FROM languages'
    return database.getFromServer(sql)

#genders
def gendersList():
    sql = 'SELECT id, RU, EN, UA FROM genders'
    return database.getFromServer(sql)

#interests
def interestsList(orderby):
    sql = 'SELECT id, RU, EN, UA FROM interests ORDER BY ' + orderby + ' ASC'
    return database.getFromServer(sql)

#cities
def isCityExists(fullTitle):
    sql = 'SELECT id FROM cities WHERE fullTitle = "'+fullTitle+'"'
    if not database.getFromServer(sql):
        return False
    return True
def cityByFullTitle(fullTitle):
    sql = 'SELECT id FROM cities WHERE fullTitle = "'+fullTitle+'"'
    return database.getFromServer(sql)[0][0]

#purposes
def purposesList():
    sql = 'SELECT id, RU, EN, UA FROM purposes'
    return database.getFromServer(sql)

#Filters
def userFilters(id):
    sql = 'SELECT minAge, maxAge, maxDistance FROM userAgeFilter ua, userDistanceFilter ud where ua.userId = '+ str(id) + ' and ud.userId = '+ str(id) 
    return database.getFromServer(sql)[0]

#Filter age
def isUserAgeFilterExist(id):
    sql = 'SELECT minAge, maxAge FROM userAgeFilter where userId = '+ str(id) 
    if not database.getFromServer(sql):
        return False
    return True

def isUserDistanceFilterExist(id):
    sql = 'SELECT maxDistance FROM userDistanceFilter where userId = '+ str(id) 
    if not database.getFromServer(sql):
        return False
    return True

#userInterestsFilter
def isUserInterestsFilterExist(id):
    sql = 'SELECT userId, interestId FROM userInterestsFilter where userId = '+ str(id) 
    if not database.getFromServer(sql):
        return False
    return True

def userInterestsFilter(id):
    sql = 'SELECT userId, interestId FROM userInterestsFilter where userId = '+ str(id)
    return database.getFromServer(sql)

def userInterestsWordsFilter(id):
    language = clientLanguage(id)
    interest = ''

    if language=="Ukrainian":
        interest='UA'
    elif language=="Russian":
        interest='RU'
    elif language=="English":
        interest='EN'

    sql = ('SELECT i.'+interest+' FROM userInterestsFilter u '+
    'INNER JOIN interests i ON i.id = u.interestId '
    +' WHERE u.userId = '+ str(id))
    return database.getFromServer(sql)

def countUserInterestsFilter(id):
    sql = 'SELECT COUNT(*) FROM userInterestsFilter where userId = '+ str(id)
    return database.getFromServer(sql)[0][0]

#userGendersFilter
def isUserGendersFilterExist(id):
    sql = 'SELECT userId, genderId FROM userGendersFilter where userId = '+ str(id) 
    if not database.getFromServer(sql):
        return False
    return True

def userGendersFilter(id):
    sql = 'SELECT userId, genderId FROM userGendersFilter where userId = '+ str(id)
    return database.getFromServer(sql)

def userGendersWordsFilter(id):
    language = clientLanguage(id)
    gender = ''

    if language=="Ukrainian":
        gender='UA'
    elif language=="Russian":
        gender='RU'
    elif language=="English":
        gender='EN'

    sql = ('SELECT g.'+gender+' FROM userGendersFilter u '+
    'INNER JOIN genders g ON g.id = u.genderId '
    +' WHERE u.userId = '+ str(id))
    return database.getFromServer(sql)

def countUserGendersFilter(id):
    sql = 'SELECT COUNT(*) FROM userGendersFilter where userId = '+ str(id)
    return database.getFromServer(sql)[0][0]

# Show likes
def countUserNewLikes(id):
    sql = 'SELECT COUNT(firstUserId) FROM userActions WHERE isLike = 1 AND secondUserId = '+ str(id) 
    return database.getFromServer(sql)[0][0]

def userNewLikes(id):
    sql = 'SELECT firstUserId FROM userActions WHERE isLike = 1 AND secondUserId = '+ str(id) 
    return database.getFromServer(sql)[0][0]



#SEARCH 
def userIdByUserFilters(id):
    sql = ('SELECT u.id, '+
       '(ST_Distance_Sphere(point(c.longitude, c.latitude), point(uu.lon, uu.lat ))/1000) as userDistance, '+
       'u.activity '+
       'FROM users u '+

            'INNER JOIN cities c ON u.cityId = c.id '+
'INNER JOIN userAgeFilter af ON af.userId = u.id '+
'INNER JOIN userDistanceFilter df ON df.userId = u.id '+

'INNER JOIN (SELECT u2.id as id, c2.longitude as lon, c2.latitude as lat, af2.minAge as minage, af2.maxAge as maxage, u2.age as age, df2.maxDistance as maxdist, u2.genderId as gender '+
            'FROM users u2 '+
            'INNER JOIN cities c2 ON u2.cityId = c2.id '+
            'INNER JOIN userAgeFilter af2 ON af2.userId = u2.id '+
            'INNER JOIN userDistanceFilter df2 ON df2.userId = u2.id '+
            'WHERE u2.id = '+ str(id)+') uu '+

'WHERE u.id <> uu.id AND '+
      'u.age >= uu.minage AND u.age <= uu.maxage AND '+
      'uu.age >= af.minAge AND uu.age <= af.maxAge AND '+
      'df.maxDistance >= (ST_Distance_Sphere(point(c.longitude, c.latitude), point(uu.lon, uu.lat ))/1000) AND '+
      'uu.maxdist >= (ST_Distance_Sphere(point(c.longitude, c.latitude), point(uu.lon, uu.lat ))/1000) AND '+
      '(uu.id, u.id) NOT IN (SELECT firstUserId, secondUserId FROM userActions WHERE firstUserId=uu.id AND secondUserId=u.id) AND '+
      '(u.id, uu.id) NOT IN (SELECT firstUserId, secondUserId FROM userActions WHERE firstUserId=u.id AND secondUserId=uu.id) AND '+

      #--if exist genderfilter for u
      '(uu.gender IN (SELECT genderId FROM userGendersFilter WHERE userId=u.id) OR (SELECT COUNT(genderId) FROM userGendersFilter WHERE userId=u.id)=0) AND '+
      #--if exist genderfilter for uu
      '(u.genderId IN (SELECT genderId FROM userGendersFilter WHERE userId=uu.id) OR (SELECT COUNT(genderId) FROM userGendersFilter WHERE userId=uu.id)=0) AND '+

      #--if exist genderfilter for uu
      '((SELECT interestId FROM userInterestsFilter WHERE userId=uu.id) IN (SELECT interestId FROM userInterests WHERE userId=u.id) OR (SELECT COUNT(interestId) FROM userInterestsFilter WHERE userId=uu.id)=0) '+

'ORDER BY (ST_Distance_Sphere(point(c.longitude, c.latitude), point(uu.lon, uu.lat ))/1000) ASC, '+
         'u.activity DESC '+
         
'LIMIT 1;')

    return database.getFromServer(sql)