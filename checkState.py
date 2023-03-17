import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import get, set, generatekeyboard, delete
from textlist import text_list as tl
import show

def nextState(id, bot, username):

    #Create account
    if not get.isAccountExist(id):
        set.createUser(id)
        nextState(id, bot, username)

    #User is none
    elif get.clientLanguage(id) == None:
        set.userState(id, "setlang")
        bot.send_message(id, 'Choose bot language, you can change it later', reply_markup=generatekeyboard.languageKeyboard())

    elif get.username(id) == None:
        if username == "None":
            set.userState(id, "setusername")
            bot.send_message(id, tl[get.clientLanguage(id)]['nousername'], reply_markup=generatekeyboard.repeatKeyboard(id))
        else:
            set.username(id,username)
            nextState(id, bot, username)

    elif get.name(id) == None:
        set.userState(id, "setname")
        bot.send_message(id, tl[get.clientLanguage(id)]['setname'])

    elif get.description(id) == None:
        set.userState(id, "setdesc")
        bot.send_message(id, tl[get.clientLanguage(id)]['setdesc'], reply_markup=generatekeyboard.skipDescriptionKeyboard(id))

    elif get.age(id)==None:
        set.userState(id, "setage")
        bot.send_message(id, tl[get.clientLanguage(id)]['setage'])

    elif get.genderId(id) == None:
        set.userState(id, "setgender")
        bot.send_message(id, tl[get.clientLanguage(id)]['setgender'], reply_markup=generatekeyboard.genderKeyboard(id))

    elif get.cityId(id) == None:
        set.userState(id, "setcity")
        bot.send_message(id, tl[get.clientLanguage(id)]['setcity'])

    elif get.purposeId(id) == None:
        set.userState(id, "setpurpose")
        bot.send_message(id, tl[get.clientLanguage(id)]['setpurpose'], reply_markup=generatekeyboard.purposeKeyboard(id))

    elif not get.isUserInterestsExist(id):
        set.userState(id, "setuserinterests")
        bot.send_message(id, tl[get.clientLanguage(id)]['setuserinterests'], reply_markup=generatekeyboard.interestsKeyboard(id))

    elif get.imageAdded(id)==None:
        set.userState(id, "setphoto")
        bot.send_message(id, tl[get.clientLanguage(id)]['setphoto'])

    #Filters are none
    elif not get.isUserAgeFilterExist(id):
        min=0
        max=0
        if int(get.age(id))-2 >= 10:
            min = int(get.age(id))-2
        else:
            min = 10

        if int(get.age(id))+2 <= 100:
            max = int(get.age(id))+2
        else:
            max = 100
        set.userAgeFilter(id, min, max)
        nextState(id, bot, username)

    elif not get.isUserDistanceFilterExist(id):
        set.userDistanceFilter(id, 0)
        nextState(id, bot, username)

    #Print user
    else:
        set.userState(id, "mainmenu")
        show.userprofile(id, bot)

# user 
def setLang(id, bot):
    set.userState(id, "setlang")
    bot.send_message(id, 'Choose bot language, you can change it later', reply_markup=generatekeyboard.languageKeyboard())

def setName(id, bot):
    set.userState(id, "setname")
    bot.send_message(id, tl[get.clientLanguage(id)]['setname'])

def setDesc(id, bot):
    set.userState(id, "setdesc")
    bot.send_message(id, tl[get.clientLanguage(id)]['setdesc'], reply_markup=generatekeyboard.skipDescriptionKeyboard(id))

def setAge(id, bot):
    set.userState(id, "setage")
    bot.send_message(id, tl[get.clientLanguage(id)]['setage'])

def setGenderId(id, bot):
    set.userState(id, "setgender")
    bot.send_message(id, tl[get.clientLanguage(id)]['setgender'], reply_markup=generatekeyboard.genderKeyboard(id))

def setCityId(id, bot):
    set.userState(id, "setcity")
    bot.send_message(id, tl[get.clientLanguage(id)]['setcity'])

def setPurposeId(id, bot):
    set.userState(id, "setpurpose")
    bot.send_message(id, tl[get.clientLanguage(id)]['setpurpose'], reply_markup=generatekeyboard.purposeKeyboard(id))

def setUserInterests(id, bot):
    set.userState(id, "setuserinterests")
    bot.send_message(id, tl[get.clientLanguage(id)]['setuserinterests'], reply_markup=generatekeyboard.interestsKeyboard(id))

def setPhoto(id, bot):
    set.userState(id, "setphoto")
    bot.send_message(id, tl[get.clientLanguage(id)]['setphoto'])

#Filters
def setMinAgeFilter(id, bot):
    set.userState(id, "setminagefilter")
    bot.send_message(id, tl[get.clientLanguage(id)]['setminagefilter'])

def setMaxAgeFilter(id, bot):
    set.userState(id, "setmaxagefilter")
    bot.send_message(id, tl[get.clientLanguage(id)]['setmaxagefilter'])

def setMaxDistanceFilter(id, bot):
    set.userState(id, "setmaxdistancefilter")
    bot.send_message(id, tl[get.clientLanguage(id)]['setmaxdistancefilter'])

def setGenderFilter(id, bot):
    set.userState(id, "setgenderfilter")
    bot.send_message(id, tl[get.clientLanguage(id)]['setgenderfilter'], reply_markup=generatekeyboard.gendersFilterKeyboard(id))

def setInterestsFilter(id, bot):
    set.userState(id, "setinterestsfilter")
    bot.send_message(id, tl[get.clientLanguage(id)]['setinterestsfilter'], reply_markup=generatekeyboard.interestsFilterKeyboard(id))

def dailyFunc():
    set.updateAllUsersActivity()
    delete.usersActions()
