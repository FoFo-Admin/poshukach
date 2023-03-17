import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import get, set
from textlist import text_list as tl

def languageKeyboard():
    languages = get.languagesList()
    markup = InlineKeyboardMarkup()

    for item in languages:
        markup.row(InlineKeyboardButton(item[0], callback_data="lang="+item[0]))

    return markup

def repeatKeyboard(id):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['repeat'], callback_data='back'))
    return markup

def skipDescriptionKeyboard(id):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['skipdesc'], callback_data='skipdesc'))
    return markup

def genderKeyboard(id):
    language = get.clientLanguage(id)
    genders = get.gendersList()
    markup = InlineKeyboardMarkup()

    for item in genders:
        if language=="Ukrainian":
            markup.row(InlineKeyboardButton(item[3], callback_data="gender="+str(item[0])))
        elif language=="Russian":
            markup.row(InlineKeyboardButton(item[1], callback_data="gender="+str(item[0])))
        elif language=="English":
            markup.row(InlineKeyboardButton(item[2], callback_data="gender="+str(item[0])))

    return markup

def purposeKeyboard(id):
    language = get.clientLanguage(id)
    genders = get.purposesList()
    markup = InlineKeyboardMarkup()

    for item in genders:
        if language=="Ukrainian":
            markup.row(InlineKeyboardButton(item[3], callback_data="purpose="+str(item[0])))
        elif language=="Russian":
            markup.row(InlineKeyboardButton(item[1], callback_data="purpose="+str(item[0])))
        elif language=="English":
            markup.row(InlineKeyboardButton(item[2], callback_data="purpose="+str(item[0])))

    return markup

def interestsKeyboard(id):
    language = get.clientLanguage(id)
    userinterests = get.userInterests(id)
    markup = InlineKeyboardMarkup()

    if language=="Ukrainian":
        interests = get.interestsList('UA')
    elif language=="Russian":
        interests = get.interestsList('RU')
    elif language=="English":
        interests = get.interestsList('EN')

    checker=False

    for item in interests:
        if language=="Ukrainian":
            checker = False
            for useritem in userinterests:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[3], callback_data="interest="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[3], callback_data="interest="+str(item[0])+"=no"))

        elif language=="Russian":
            checker = False
            for useritem in userinterests:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[1], callback_data="interest="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[1], callback_data="interest="+str(item[0])+"=no"))

        elif language=="English":
            checker = False
            for useritem in userinterests:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[2], callback_data="interest="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[2], callback_data="interest="+str(item[0])+"=no"))

    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['interestsDone'], callback_data='interestsDone'))
    return markup

def interestsFilterKeyboard(id):
    language = get.clientLanguage(id)
    userinterests = get.userInterestsFilter(id)
    markup = InlineKeyboardMarkup()

    if language=="Ukrainian":
        interests = get.interestsList('UA')
    elif language=="Russian":
        interests = get.interestsList('RU')
    elif language=="English":
        interests = get.interestsList('EN')

    checker=False

    for item in interests:
        if language=="Ukrainian":
            checker = False
            for useritem in userinterests:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[3], callback_data="interest="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[3], callback_data="interest="+str(item[0])+"=no"))
        elif language=="Russian":
            checker = False
            for useritem in userinterests:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[1], callback_data="interest="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[1], callback_data="interest="+str(item[0])+"=no"))

        elif language=="English":
            checker = False
            for useritem in userinterests:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[2], callback_data="interest="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[2], callback_data="interest="+str(item[0])+"=no"))

    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['interestsDone'], callback_data='interestsDone'))
    return markup

def gendersFilterKeyboard(id):
    language = get.clientLanguage(id)
    usergenders = get.userGendersFilter(id)
    markup = InlineKeyboardMarkup()
    genders = get.gendersList()

    checker=False

    for item in genders:
        if language=="Ukrainian":
            checker = False
            for useritem in usergenders:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[3], callback_data="genders="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[3], callback_data="genders="+str(item[0])+"=no"))
        elif language=="Russian":
            checker = False
            for useritem in usergenders:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[1], callback_data="genders="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[1], callback_data="genders="+str(item[0])+"=no"))
        elif language=="English":
            checker = False
            for useritem in usergenders:
                if useritem[1] == item[0]:
                    markup.row(InlineKeyboardButton('✔️'+item[2], callback_data="genders="+str(item[0])+"=yes"))
                    checker = True
            if not checker:
                markup.row(InlineKeyboardButton('❌'+item[2], callback_data="genders="+str(item[0])+"=no"))

    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['gendersDone'], callback_data='gendersDone'))
    return markup

def changeMenuKeyboard(id):
    markup = InlineKeyboardMarkup()

    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setlangbtn'], callback_data='setlangbtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setnamebtn'], callback_data='setnamebtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setdescbtn'], callback_data='setdescbtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setagebtn'], callback_data='setagebtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setgenderbtn'], callback_data='setgenderbtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setcitybtn'], callback_data='setcitybtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setpurposebtn'], callback_data='setpurposebtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setuserinterestsbtn'], callback_data='setuserinterestsbtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['setphotobtn'], callback_data='setphotobtn'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['deleteprofile'], callback_data='deleteprofile'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['back'], callback_data='back'))

    return markup

def filterKeyboard(id):
    markup = InlineKeyboardMarkup()

    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['changeminagefilter'], callback_data='changeminagefilter'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['changemaxagefilter'], callback_data='changemaxagefilter'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['changemaxdestancefilter'], callback_data='changemaxdestancefilter'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['changegenderfilter'], callback_data='changegenderfilter'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['changeinterestsfilter'], callback_data='changeinterestsfilter'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['back'], callback_data='back'))

    return markup

def likemenu(id):
    markup = InlineKeyboardMarkup()

    markup.row(InlineKeyboardButton("👍", callback_data='like'), InlineKeyboardButton("👎", callback_data='dislike'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['back'], callback_data='back'))

    return markup

def likeOrDislike(id, isLike):
    markup = InlineKeyboardMarkup()

    if isLike:
         markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['yousetlik'], callback_data='none'))
    else:
        markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['yousetdis'], callback_data='none'))

    return markup

def mainMenuKeyboard(id):
    markup = InlineKeyboardMarkup()

    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['startsearching'], callback_data='startsearching'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['changeprofile'], callback_data='changeprofile'))
    markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['myfilters'], callback_data='myfilters'))
    if int(get.countUserNewLikes(id)) != 0:
        markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['mynewlikes']+str(get.countUserNewLikes(id)), callback_data='mynewlikes'))
    else: 
        markup.row(InlineKeyboardButton(tl[get.clientLanguage(id)]['nonewlikes'], callback_data='nonewlikes'))

    return markup

