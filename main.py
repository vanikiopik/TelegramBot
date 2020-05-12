import time
import telepot
# Should back here aftrer!!! import emojis
import random
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
ActiveUsers = []
BotApi = "970142854:AAG_1bcT9hicWcfuApo7swz_mqkqZ4pOyjY"
bot = telepot.Bot(BotApi)
Graphic = ["ВВЕРХ", "ВНИЗ"]
Peak = ["От просадки", "От пика"]
text = '''High The Money | Binomo Bot:
Внимание! 
Использование бота - риск! 
Автор данного бота никаким образом не обещает Вам 100% получения прибыли и снимает с  
себя всю ответственность за сохранность Ваших денежных средств! 
Это бинарные опционы - Вы можете как прeумножить, так и проиграть свои средства.'''
TimeMin = '''1 минута
'''
KeyboardMenuFirst = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ᅠᅠМенюᅠᅠ')],
                                                  [KeyboardButton(text='О нас')],
                                                  [KeyboardButton(text='Условия получения доступа к боту')]], resize_keyboard=True)
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
            bot.sendMessage(chat_id, 'High The Money | OlympTrade Bot:\n'
                                     'Здраствуйте,введите ключ,полученый у @OTRBot_support', reply_markup=KeyboardMenuFirst)

        if msg['text'] == 'ᅠᅠМенюᅠᅠ':
            bot.sendMessage(chat_id, 'High The Money | OlympTrade Bot:\n'
                                     'Для получения доступа введите ключ,\n'
                                     'полученный у @OTRBot_support')

        if msg['text'] == 'Условия получения доступа к боту':
            bot.sendMessage(chat_id, 'High The Money | OlympTrade Bot:\n'
                                     'I. Бот доступен  для жителей Беларуси, Украины и Казахстана\n'
                                     '    (Можно использовать VPN)\n'
                                     'II. Вы должны зарегестрироваться по ссылке,предоставленной\n'
                                     '    администратором @OTRBot_support и сделать депозит на свой счёт\n'
                                     '    от 10$.\n'
                                     'В итоге вы получаете свой личный пароль для пользования функционалом бота.\n'
                                     'P.S: Доступ к боту неограничен. Функционал бота будет совершенстоваваться.\n')


        if msg['text'] == 'TFxNhhwVET4O':
            bot.sendMessage(chat_id, 'Поздравляем!Вы получили доступ к боту.', reply_markup=KeyboardMenuSecond)

        if msg['text'] == 'ᅠᅠᅠМенюᅠᅠᅠ':
            bot.sendMessage(chat_id, 'Выберите валютную пару для торговли:', reply_markup=KeyboardMain)

        if msg['text'] == 'О нас':
            bot.sendMessage(chat_id, 'High The Money | OlympTrade Bot:\n'
                                     'Мы - маленькая команда разработчиков, \n'
                                     'разработавщая сигнал-бота,дающего стабильную прибыль на\n'
                                     ' прогнозах курса различных валютных рынков.\n'
                                     'Данный бот - искусственный интелект,которой был обучен \n'
                                     'анализировать весь рынок и делать прогнозы,исходя из рыночной линии тренда.\n'
                                     'Он использует специальный OTR_key 3.4.1, с помощью\n'
                                     ' которого прогнозы поступают к пользователю мгновенно. \n'
                                     'Статистика за октябрь 2019 - апрель 2020:\n'
                                     'Успешность прогноза составляет 83.56%\n')

        if msg['text'] == 'Сообщение о рисках':
                bot.sendMessage(chat_id, text, reply_markup=KeyboardMain)

        # ВВЕРХ + ОТ ПИКА
        if msg['text'] == 'EUR/USD' and scale == "ВВЕРХ" and rise == "От пика":
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
        # ВВЕРХ + ОТ ПРОСАДКИ
        if msg['text'] == 'EUR/USD' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'USD/JPY' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'AUD/CAD' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'EUR/CAD' and scale == "ВВЕРХ" and rise == "От просадкиа":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'GBP/USD' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        if msg['text'] == 'BTC' and scale == "ВВЕРХ" and rise == "От просадки":
                bot.sendMessage(chat_id, msg['text']+'''\n'''+TimeMin+''''''+scale+'''\n'''+rise, reply_markup=KeyboardMain)
        # ВНИЗ + ОТ ПИКА
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
        # ВНИЗ + ОТ ПРОСАДКИ
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
# Checking types of messages

MessageLoop  (bot,  {
    'chat': on_chat_message,
                    }).run_as_thread()

# Always still on work
while 1:
    time.sleep(10)