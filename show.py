import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import get, set, generatekeyboard
from textlist import text_list as tl
import checkState as cs

def userprofile(id, bot):
    user = get.userInfo(id)
    userinterests = get.userInterestsWords(id)

    string = '<b>' + user[0] + '</b> ' + str(user[2]) + '\n\n' + user[3] + '\n\n' + user[4] + '\n\n' + user[1] + '\n\n<b>'+ tl[get.clientLanguage(id)]['showinterests'] +':</b> '

    for item in userinterests:
        string += item[0]+", "

    bot.send_photo(id, photo=open('userPhotos/user' + str(id) + '.jpg', 'rb'), caption=string[:-2], parse_mode='HTML', reply_markup=generatekeyboard.mainMenuKeyboard(id))

def userfilters(id, bot):
    userfilters = get.userFilters(id)
    
    string = ('<b>'+tl[get.clientLanguage(id)]['agefilter']+'</b>: '+str(userfilters[0])+'-'+str(userfilters[1])+'\n\n'
             +'<b>'+tl[get.clientLanguage(id)]['distancefilter']+'</b>: '+str(userfilters[2])+' '+tl[get.clientLanguage(id)]['km']+'\n\n'
             +'<b>'+tl[get.clientLanguage(id)]['genderfilter']+'</b>: ')

    if get.isUserGendersFilterExist(id):
        userGendersFilter = get.userGendersWordsFilter(id)
        for item in userGendersFilter:
            string += item[0]+", "
        string = string[:-2]
    else:
        string+=tl[get.clientLanguage(id)]['nogenderfilter']

    string+='\n\n<b>'+tl[get.clientLanguage(id)]['interestfilter']+'</b>: '

    if get.isUserInterestsFilterExist(id):
        userInterestsFilter = get.userInterestsWordsFilter(id)
        for item in userInterestsFilter:
            string += item[0]+", "
        string = string[:-2]
    else: 
        string+=tl[get.clientLanguage(id)]['nointerestfilter']

    bot.send_message(id, string, parse_mode='HTML', reply_markup=generatekeyboard.filterKeyboard(id))

def showUsers(id, bot, username):
    if(get.username(id) != username):
        if username == 'None':
            set.usernameNULL(id)
            cs.nextState(id, bot, username)

    userinfo = get.userIdByUserFilters(id)
    if userinfo: 
        user = get.userInfo(userinfo[0][0])    
        userinterests = get.userInterestsWords(userinfo[0][0])

        string = '<b>' + user[0] + '</b> ' + str(user[2]) + '\n\n' + user[3] + '\n\n' + user[4] + '\n\n' + user[1] + '\n\n<b>'+ tl[get.clientLanguage(id)]['showinterests'] +':</b> '

        for item in userinterests:
            string += item[0]+", "

        set.userState(id, "lookat="+str(userinfo[0][0]))

        bot.send_photo(id, photo=open('userPhotos/user' + str(userinfo[0][0]) + '.jpg', 'rb'), caption=string[:-2], parse_mode='HTML', reply_markup=generatekeyboard.likemenu(id))
    else:
        bot.send_message(id, tl[get.clientLanguage(id)]['nopeople'], parse_mode='HTML')
        cs.nextState(id, bot, username)


def lookAtLikes(id, bot):
    if int(get.countUserNewLikes(id)) != 0:
        userinfo = get.userNewLikes(id)
        user = get.userInfo(userinfo)    
        userinterests = get.userInterestsWords(userinfo)

        string = '<b>' + user[0] + '</b> ' + str(user[2]) + '\n\n' + user[3] + '\n\n' + user[4] + '\n\n' + user[1] + '\n\n<b>'+ tl[get.clientLanguage(id)]['showinterests'] +':</b> '

        for item in userinterests:
            string += item[0]+", "

        set.userState(id, "lookatlike="+str(userinfo))

        bot.send_photo(id, photo=open('userPhotos/user' + str(userinfo) + '.jpg', 'rb'), caption=string[:-2], parse_mode='HTML', reply_markup=generatekeyboard.likemenu(id))
    else:
        bot.send_message(id, tl[get.clientLanguage(id)]['nomorelikes'], parse_mode='HTML')
        cs.nextState(id, bot, get.username(id))

def sendMutually(firstId, secondId, bot):
    user = get.userInfo(firstId)
    userinterests = get.userInterestsWords(firstId)

    string = tl[get.clientLanguage(secondId)]['newmutual'] +'\n<a href="t.me/'+get.username(firstId)+'">' + user[0] + '</a> ' + str(user[2]) + '\n\n' + user[3] + '\n\n' + user[4] + '\n\n' + user[1] + '\n\n<b>'+ tl[get.clientLanguage(secondId)]['showinterests'] +':</b> '

    for item in userinterests:
        string += item[0]+", "

    bot.send_photo(secondId, photo=open('userPhotos/user' + str(firstId) + '.jpg', 'rb'), caption=string[:-2], parse_mode='HTML')
###################################
    user = get.userInfo(secondId)
    userinterests = get.userInterestsWords(secondId)

    string = tl[get.clientLanguage(firstId)]['newmutual'] +'\n<a href="t.me/'+get.username(secondId)+'">' + user[0] + '</a> ' + str(user[2]) + '\n\n' + user[3] + '\n\n' + user[4] + '\n\n' + user[1] + '\n\n<b>'+ tl[get.clientLanguage(firstId)]['showinterests'] +':</b> '

    for item in userinterests:
        string += item[0]+", "

    bot.send_photo(firstId, photo=open('userPhotos/user' + str(secondId) + '.jpg', 'rb'), caption=string[:-2], parse_mode='HTML')