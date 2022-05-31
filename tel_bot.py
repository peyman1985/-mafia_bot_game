# -*- coding:utf-8 -*-
from random import shuffle

import unicodedata
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update
from telegram.ext import Updater , CommandHandler,CallbackQueryHandler
token=Updater('',use_context=True)
username_dic = {}
print(username_dic)
readers= []
def gamestart(update,context):
    global readers
    # readers=shuffle(readers)
    # GOD = 123456789
    # MAFIA     = readers[0:4]
    # CITY      = readers[4:]
    # GODFATHER = MAFIA[0]
    # MAFIAONE  = MAFIA[1]
    # MAFIATWO  = MAFIA[2]
    # MAFITREE  = MAFIA[3]
    # DOCTOR    = CITY[0]
    # DETECTIVE = CITY[1]
    # ARMER     = CITY[2]
    # CITYONE   = CITY[3]
    # CITYTWO   = CITY[4]
    # CITYTHREE = CITY[5]
    query = update.callback_query
    context.bot.send_message(chat_id =query.message.chat_id,text='شروع بازی')
    context.bot.send_message(chat_id =query.message.chat_id,text='اسامی بازیکنان ')
    for id,username in username_dic.items():
        context.bot.send_message(chat_id =query.message.chat_id,text=f'نام بازیکن :{username}')
        context.bot.send_message(url=f'http://t.me{}',text=f'نام بازیکن :{username}')

    context.bot.send_message(chat_id =query.message.chat_id,text='نقش  برای شما ارسال شد ')


def start(update,context):
    key = [[InlineKeyboardButton('اعلام امادگی برای ورود به بازی',callback_data='1')],[InlineKeyboardButton('لغو امادگی',callback_data='2')]]
    key1 = InlineKeyboardMarkup(key)
    context.bot.send_message(chat_id = update.message.chat_id,text='به شب مافیا خوش امدین 🌌',reply_markup = key1)
def handler_readers(update,context):

    global readers
    query = update.callback_query
    ui = update.callback_query.from_user.id
    print(update.callback_query.from_user.first_name)
    if query.data =='1':
        if ui in readers:
            context.bot.send_message(update.callback_query.message.chat_id,text=f'{update.callback_query.from_user.first_name}شما  قبلا اعلام امادگی کردید')
        elif ui not in readers:
            context.bot.send_message(update.callback_query.message.chat_id,text=f'{update.callback_query.from_user.first_name}آمادگی شما ثبت شد✅')
            readers.append(ui)
            username_dic[ui]=update.callback_query.from_user.first_name
            print(readers)
            if len(readers)==2:
                gamestart(update,context)
    elif query.data =='2':
        if ui in readers:
            context.bot.send_message(update.callback_query.message.chat_id,text='شما از لیست شهر حذف شدین')
            readers.remove(ui)
            print(readers)
        elif ui not in readers:
            context.bot.send_message(update.callback_query.message.chat_id,text='شما عضو شهر نشده اید')




token.dispatcher.add_handler(CommandHandler('start',start))
token.dispatcher.add_handler(CallbackQueryHandler(handler_readers))


token.start_polling()
token.idle()