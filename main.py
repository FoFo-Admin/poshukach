import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import database, get, set, delete, generatekeyboard, show
from textlist import text_list as tl
import requests, json
import checkState as cs


API_TOKEN = ''
OPENCAGE_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

#######################################
# Commands
@bot.message_handler(commands=['start'])
def startCommand(message):
    if message.chat.id > 0:
        cs.nextState(message.from_user.id, bot, str(message.from_user.username))

###############################
# Text controller
@bot.message_handler(content_types=['text'])
def textController(message):
    if message.chat.id > 0:
        if get.state(message.from_user.id) == "setname":
            if (len(message.text) >= 2 and len(message.text) <= 50):
                set.name(message.from_user.id, message.text)
                cs.nextState(message.from_user.id, bot, str(message.from_user.username))
            else: 
                bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['nameerror']+str(len(message.text)))

        elif get.state(message.from_user.id) == "setdesc":
            if (len(message.text) >= 2 and len(message.text) <= 1000):
                set.description(message.from_user.id, message.text)
                cs.nextState(message.from_user.id, bot, str(message.from_user.username))
            else: 
                bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['deskerror']+str(len(message.text)))

        elif get.state(message.from_user.id) == "setage":
            if message.text.isdigit():
                if (int(message.text) >= 10 and int(message.text) <= 100):
                    set.age(message.from_user.id, message.text)
                    cs.nextState(message.from_user.id, bot, str(message.from_user.username))
                else: 
                    bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['ageerror'])
            else: 
                bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['ageerror'])

        elif get.state(message.from_user.id) == "setcity":
            response = requests.get("https://api.opencagedata.com/geocode/v1/json?q="+message.text+"&key="+OPENCAGE_TOKEN+"&language=native&pretty=1")
            if response.json()['results']:
                set.cityId(message.from_user.id, response)
                cs.nextState(message.from_user.id, bot, str(message.from_user.username))
            else: 
                bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['cityerror'])   

        elif get.state(message.from_user.id) == "setminagefilter":
            if message.text.isdigit():
                if (int(message.text) >= 10 and int(message.text) <= int(get.userFilters(message.from_user.id)[1])):
                    set.userMinAgeFilter(message.from_user.id, message.text)
                    cs.nextState(message.from_user.id, bot, str(message.from_user.username))
                else: 
                    bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['minagefiltererror'])
            else: 
                bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['minagefiltererror'])

        elif get.state(message.from_user.id) == "setmaxagefilter":
            if message.text.isdigit():
                if (int(message.text) <= 100 and int(message.text) >= int(get.userFilters(message.from_user.id)[0])):
                    set.userMaxAgeFilter(message.from_user.id, message.text)
                    cs.nextState(message.from_user.id, bot, str(message.from_user.username))
                else: 
                    bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['maxagefiltererror'])
            else: 
                bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['maxagefiltererror'])

        elif get.state(message.from_user.id) == "setmaxdistancefilter":
            if message.text.isdigit():
                if (int(message.text) >= 0 and int(message.text) <= 1500):
                    set.userMaxDistanceFilter(message.from_user.id, message.text)
                    cs.nextState(message.from_user.id, bot, str(message.from_user.username))
                else: 
                    bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['maxdistancefiltererror'])
            else: 
                bot.send_message(message.chat.id, tl[get.clientLanguage(message.from_user.id)]['maxdistancefiltererror'])

        else:
            bot.send_message(message.from_user.id, tl[get.clientLanguage(message.from_user.id)]['unknown_command'])
            

#######################################
# Callback controller
@bot.callback_query_handler(func=lambda call: call.data == "none")
def noneSet(call):
    a=0

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    if call.from_user.id > 0:
        cs.nextState(call.from_user.id, bot, str(call.from_user.username))

@bot.callback_query_handler(func=lambda call: call.data == "deleteprofile")
def deleteprofile(call):
    if call.from_user.id > 0:
        delete.user(call.from_user.id)
        cs.nextState(call.from_user.id, bot, str(call.from_user.username))

@bot.callback_query_handler(func=lambda call: call.data == "skipdesc")
def skipDesc(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "setdesc":
            set.description(call.from_user.id, ' ')
            cs.nextState(call.from_user.id, bot, str(call.from_user.username))

@bot.callback_query_handler(func=lambda call: call.data == "gendersDone")
def interestsDone(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "setgenderfilter":
            cs.nextState(call.from_user.id, bot, str(call.from_user.username))  

@bot.callback_query_handler(func=lambda call: call.data == "interestsDone")
def interestsDone(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "setuserinterests":
            if int(get.countUserInterests(call.from_user.id)) >= 1:
                cs.nextState(call.from_user.id, bot, str(call.from_user.username))
            else:
                bot.send_message(call.from_user.id, tl[get.clientLanguage(call.from_user.id)]['userinterestserror'])   
        elif get.state(call.from_user.id) == "setinterestsfilter":
            cs.nextState(call.from_user.id, bot, str(call.from_user.username))  

@bot.callback_query_handler(func=lambda call: call.data == "changeprofile")
def changeProfile(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "mainmenu":
            set.userState(call.from_user.id, "changemenu") 
            bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.id, reply_markup=generatekeyboard.changeMenuKeyboard(call.from_user.id))

@bot.callback_query_handler(func=lambda call: call.data == "setlangbtn")
def setlangbtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setLang(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "setnamebtn")
def setnamebtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setName(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "setdescbtn")
def setdescbtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setDesc(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "setagebtn")
def setagebtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setAge(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "setgenderbtn")
def setgenderbtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setGenderId(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "setcitybtn")
def setcitybtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setCityId(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "setpurposebtn")
def setpurposebtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setPurposeId(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "setuserinterestsbtn")
def setuserinterestsbtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setUserInterests(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "setphotobtn")
def setphotobtn(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "changemenu":
            cs.setPhoto(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "myfilters")
def myFilters(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "mainmenu":
            set.userState(call.from_user.id, "filtermenu") 
            show.userfilters(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "changeminagefilter")
def changeminagefilter(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "filtermenu":
            cs.setMinAgeFilter(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "changemaxagefilter")
def changemaxagefilter(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "filtermenu":
            cs.setMaxAgeFilter(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "changemaxdestancefilter")
def changemaxdestancefilter(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "filtermenu":
            cs.setMaxDistanceFilter(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "changegenderfilter")
def changegenderfilter(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "filtermenu":
            cs.setGenderFilter(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "changeinterestsfilter")
def changeinterestsfilter(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "filtermenu":
            cs.setInterestsFilter(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "startsearching")
def startsearching(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id) == "mainmenu":
            show.showUsers(call.from_user.id, bot, str(call.from_user.username))

@bot.callback_query_handler(func=lambda call: call.data == "dislike")
def dislike(call):
    if call.from_user.id > 0:
        if "=" in get.state(call.from_user.id):
            if get.state(call.from_user.id).split("=")[0] == "lookat":
                bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.id, reply_markup=generatekeyboard.likeOrDislike(call.from_user.id, False))
                set.likeordislike(call.from_user.id, get.state(call.from_user.id).split("=")[1], 0)
                set.plusUserActivity(call.from_user.id)
                show.showUsers(call.from_user.id, bot, str(call.from_user.username))

            elif get.state(call.from_user.id).split("=")[0] == "lookatlike":
                bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.id, reply_markup=generatekeyboard.likeOrDislike(call.from_user.id, False))
                set.changeLikeToFalse(call.from_user.id, get.state(call.from_user.id).split("=")[1])
                show.lookAtLikes(call.from_user.id, bot)

@bot.callback_query_handler(func=lambda call: call.data == "like")
def like(call):
    if call.from_user.id > 0:
        if "=" in get.state(call.from_user.id):
            if get.state(call.from_user.id).split("=")[0] == "lookat":
                bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.id, reply_markup=generatekeyboard.likeOrDislike(call.from_user.id, True))
                set.likeordislike(call.from_user.id, get.state(call.from_user.id).split("=")[1], 1)
                set.plusUserActivity(call.from_user.id)
                bot.send_message(get.state(call.from_user.id).split("=")[1], tl[get.clientLanguage(get.state(call.from_user.id).split("=")[1])]['yougetlike']) 
                show.showUsers(call.from_user.id, bot, str(call.from_user.username))

            elif get.state(call.from_user.id).split("=")[0] == "lookatlike":
                bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.id, reply_markup=generatekeyboard.likeOrDislike(call.from_user.id, True))
                set.changeLikeToFalse(call.from_user.id, get.state(call.from_user.id).split("=")[1])
                show.sendMutually(call.from_user.id, get.state(call.from_user.id).split("=")[1], bot)
                show.lookAtLikes(call.from_user.id, bot)
                
@bot.callback_query_handler(func=lambda call: call.data == "nonewlikes")
def nonewlikes(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id).split("=")[0] == "mainmenu":
            bot.send_message(call.from_user.id, tl[get.clientLanguage(call.from_user.id)]['nolike']) 

@bot.callback_query_handler(func=lambda call: call.data == "mynewlikes")
def nonewlikes(call):
    if call.from_user.id > 0:
        if get.state(call.from_user.id).split("=")[0] == "mainmenu":
           show.lookAtLikes(call.from_user.id, bot)
            


@bot.callback_query_handler(func=lambda call: True)
def callController(call):
    if call.from_user.id > 0:
        if "=" in call.data:
            if (call.data.split("=")[0] == "lang" and get.state(call.from_user.id) == "setlang"):
                set.clientLanguageId(call.from_user.id, call.data.split("=")[1])
                cs.nextState(call.from_user.id, bot, str(call.from_user.username))

            elif (call.data.split("=")[0] == "gender" and get.state(call.from_user.id) == "setgender"):
                set.genderId(call.from_user.id, call.data.split("=")[1])
                cs.nextState(call.from_user.id, bot, str(call.from_user.username))

            elif (call.data.split("=")[0] == "purpose" and get.state(call.from_user.id) == "setpurpose"):
                set.purposeId(call.from_user.id, call.data.split("=")[1])
                cs.nextState(call.from_user.id, bot, str(call.from_user.username))

            elif (call.data.split("=")[0] == "interest" and get.state(call.from_user.id) == "setuserinterests"):
                if(call.data.split("=")[2] == "no"):
                    if int(get.countUserInterests(call.from_user.id)) < 5:
                        set.userInterest(call.from_user.id, call.data.split("=")[1])
                    else: 
                        bot.send_message(call.from_user.id, tl[get.clientLanguage(call.from_user.id)]['userinterestserror2'])   
                elif(call.data.split("=")[2] == "yes"):
                    delete.userInterest(call.from_user.id, call.data.split("=")[1])
                bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.id, reply_markup=generatekeyboard.interestsKeyboard(call.from_user.id))

            elif (call.data.split("=")[0] == "interest" and get.state(call.from_user.id) == "setinterestsfilter"):
                if(call.data.split("=")[2] == "no"):
                    if int(get.countUserInterestsFilter(call.from_user.id)) < 1:
                        set.userInterestFilter(call.from_user.id, call.data.split("=")[1])
                    else: 
                        bot.send_message(call.from_user.id, tl[get.clientLanguage(call.from_user.id)]['userinterestsfiltererror2'])   
                elif(call.data.split("=")[2] == "yes"):
                    delete.userInterestFilter(call.from_user.id, call.data.split("=")[1])
                bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.id, reply_markup=generatekeyboard.interestsFilterKeyboard(call.from_user.id))

            elif (call.data.split("=")[0] == "genders" and get.state(call.from_user.id) == "setgenderfilter"):
                if(call.data.split("=")[2] == "no"):
                    set.userGenderFilter(call.from_user.id, call.data.split("=")[1]) 
                elif(call.data.split("=")[2] == "yes"):
                    delete.userGenderFilter(call.from_user.id, call.data.split("=")[1])
                bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.id, reply_markup=generatekeyboard.gendersFilterKeyboard(call.from_user.id))

#######################################
# Photo controller
@bot.message_handler(content_types=['photo'])
def imageController(message):
    if message.chat.id > 0:
        if get.state(message.from_user.id) == "setphoto":
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = 'userPhotos/user' + str(message.from_user.id) + '.jpg'
            with open(src, 'wb') as newPhoto:
                newPhoto.write(downloaded_file)
            set.imageAdded(message.from_user.id, str(1))
            cs.nextState(message.from_user.id, bot, str(message.from_user.username))


#######################################
# Polling

bot.infinity_polling()
