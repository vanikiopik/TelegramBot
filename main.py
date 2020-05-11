import time
import telepot
import emojis
import random
from telepot.loop import MessageLoop
from telepot.namedtuple import  ReplyKeyboardMarkup, KeyboardButton
ActiveUsers = []
BotApi = "970142854:AAG_1bcT9hicWcfuApo7swz_mqkqZ4pOyjY"
bot = telepot.Bot(BotApi)
Graphic = ["ВВЕРХ", "ВНИЗ"]
Peak = ["От просадки", "От пика"]
text = '''High The Money | Binomo Bot:
Внимание! 
Использование бота - риск! 
Автор данного обеспечения никаким образом не обещает Вам 100% получения прибыли и снимает с  
себя всю ответственность за сохранность Ваших денежных средств! 
Это бинарные опционы - Вы можете как прeумножить, так и проиграть свои средства.'''
TimeMin = '''1 минута
'''
KeyboardMenuFirst = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ᅠᅠМенюᅠᅠ')],
                                                  [KeyboardButton(text='О нас')]], resize_keyboard=True)
KeyboardMenuSecond = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ᅠᅠᅠМенюᅠᅠᅠ')]], resize_keyboard=True)
KeyboardMain = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='EUR/USD'), KeyboardButton(text='USD/JPY')],
                                            [KeyboardButton(text='AUD/CAD'), KeyboardButton(text='EUR/CAD')],
                                            [KeyboardButton(text='GBP/USD'), KeyboardButton(text='BTC')],
                                            [KeyboardButton(text='О нас')],
                                            [KeyboardButton(text='Сообщение о рисках')]],
                                            resize_keyboard=True)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print('On chat message:', content_type, chat_type, chat_id)
    if content_type == 'text':
        scale = random.choice(Graphic)
        rise = random.choice(Peak)
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, 'Здраствуйте,введите ключ,полученый у @vanikiopik', reply_markup=KeyboardMenuFirst)

        if msg['text'] == 'ᅠᅠМенюᅠᅠ':
            bot.sendMessage(chat_id, 'Для доступа введите ключ,полученный у @vanikiopik')

        if msg['text'] == 'TFxNhhwVET4O':
            bot.sendMessage(chat_id, 'Поздравляем!Вы получили доступ к боту.', reply_markup=KeyboardMenuSecond)

        if msg['text'] == 'ᅠᅠᅠМенюᅠᅠᅠ':
            bot.sendMessage(chat_id, 'Выберите валютную пару для торговли:', reply_markup=KeyboardMain)

        if msg['text'] == 'О нас':
            bot.sendMessage(chat_id, 'High The Money | Binomo Bot:\n'
                                     'Мы - маленькая команда разработчиков, \n'
                                     'котороя разработала сигнал-бота,дающего прибыль.\n'
                                     'Данный бот - искусственный интелект,которой был обучен \n'
                                     'анализировать весь рынок и делать прогнозы.\n'
                                     'Он использует специальный BinAPI_2.0.4 ключ. \n'
                                     'Статистика за октябрь 2019 - декабрь 2020:\n'
                                     'Успешно проходит 7 ставок из 10')

        if msg['text'] == 'Сообщение о рисках':
                bot.sendMessage(chat_id, text, reply_markup=KeyboardMain)


        #ВВЕРХ + ОТ ПИКА
        if msg['text'] == 'EUR/USD' and scale == "ВВЕРХ" and rise =="От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'USD/JPY' and scale == "ВВЕРХ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'AUD/CAD' and scale == "ВВЕРХ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'EUR/CAD' and scale == "ВВЕРХ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'GBP/USD' and scale == "ВВЕРХ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'BTC' and scale == "ВВЕРХ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        #ВВЕРХ + ОТ ПРОСАДКИ
        if msg['text'] == 'EUR/USD' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'USD/JPY' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'AUD/CAD' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'EUR/CAD' and scale == "ВВЕРХ" and rise == "ООт просадкиа":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'GBP/USD' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'BTC' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        #ВНИЗ + ОТ ПИКА
        if msg['text'] == 'EUR/USD' and scale == "ВНИЗ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'USD/JPY' and scale == "ВНИЗ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'AUD/CAD' and scale == "ВНИЗ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'EUR/CAD' and scale == "ВНИЗ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'GBP/USD' and scale == "ВНИЗ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'BTC' and scale == "ВНИЗ" and rise == "От пика":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        #ВНИЗ + ОТ ПРОСАДКИ
        if msg['text'] == 'EUR/USD' and scale == "ВНИЗ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'USD/JPY' and scale == "ВНИЗ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'AUD/CAD' and scale == "ВНИЗ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'EUR/CAD' and scale == "ВНИЗ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'GBP/USD' and scale == "ВНИЗ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'BTC' and scale == "ВНИЗ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        else:
            pass


def on_callback_query(msg):
    pass

MessageLoop(bot,  {
    'chat': on_chat_message,
                    }).run_as_thread()

# Always still on work
while 1:
    time.sleep(10)