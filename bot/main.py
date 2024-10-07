from asyncio import sleep
import os
import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove
import threading


TOKEN = '8043595575:AAGaXOGpD5Aj8PwJmQYT7fuWcC81RYhNXMU'
bot = telebot.TeleBot(TOKEN)

ADMIN = -1002209586070

LIST = 1000
USERS = [' '] * LIST
answers = [' '] * LIST
my_name = [' '] * LIST
my_number = [' '] * LIST
user_messages = {}



def on_click(message, USER_ID):
     global answers
     x = message.text
     if message.text == 'Bitcoin':
          answers[USER_ID] +='Валюта для обмена: Bitcoin\n'
          question_2(message, USER_ID)
          bot.register_next_step_handler(message, on_click_2, USER_ID)
     elif message.text == 'Litecoin':
          answers[USER_ID] +='Валюта для обмена: Litecoin\n'
          question_2(message, USER_ID)
          bot.register_next_step_handler(message, on_click_2, USER_ID)
     elif message.text == 'Ethereum':
          answers[USER_ID] +='Валюта для обмена: Ethereum\n'
          question_2(message, USER_ID)
          bot.register_next_step_handler(message, on_click_2, USER_ID)
     elif message.text == 'Tether':
          answers[USER_ID] +='Валюта для обмена: Tether\n'
          question_2(message, USER_ID)
          bot.register_next_step_handler(message, on_click_2, USER_ID)
     elif message.text == 'Rub':
          answers[USER_ID] +='Валюта для обмена: Rub\n'
          question_2(message, USER_ID)
          bot.register_next_step_handler(message, on_click_2, USER_ID)
     else:
          bot.send_message(message.chat.id, 'Необходимо выбрать валюту с помощью кнопок.')
          question_1(message, USER_ID)
          bot.register_next_step_handler(message, on_click, USER_ID)

def on_click_2(message, USER_ID):
     global answers
     x = message.text

     if message.text == 'Bitcoin':
          answers[USER_ID] +='Валюта для получения: Bitcoin\n'
          bot.send_message(message.chat.id, 'Введите сумму для обмена:', reply_markup=ReplyKeyboardRemove())
          bot.register_next_step_handler(message, enter_number, USER_ID)
     elif message.text == 'Litecoin':
          answers[USER_ID] +='Валюта для получения: Litecoin\n'
          bot.send_message(message.chat.id, 'Введите сумму для обмена:', reply_markup=ReplyKeyboardRemove())
          bot.register_next_step_handler(message, enter_number, USER_ID)
     elif message.text == 'Ethereum':
          answers[USER_ID] +='Валюта для получения: Ethereum\n'
          bot.send_message(message.chat.id, 'Введите сумму для обмена:', reply_markup=ReplyKeyboardRemove())
          bot.register_next_step_handler(message, enter_number, USER_ID)
     elif message.text == 'Tether':
          answers[USER_ID] +='Валюта для получения: Tether\n'
          bot.send_message(message.chat.id, 'Введите сумму для обмена:', reply_markup=ReplyKeyboardRemove())
          bot.register_next_step_handler(message, enter_number, USER_ID)
     elif message.text == 'Rub':
          answers[USER_ID] +='Валюта для получения: Rub\n'
          bot.send_message(message.chat.id, 'Введите сумму для обмена:', reply_markup=ReplyKeyboardRemove())
          bot.register_next_step_handler(message, enter_number, USER_ID)
     else:
          bot.send_message(message.chat.id, 'Необходимо выбрать валюту с помощью кнопок.')
          question_1(message, USER_ID)
          bot.register_next_step_handler(message, on_click_2, USER_ID)


def question_1(message, USER_ID):

    markup = types.ReplyKeyboardMarkup()


    button_a = types.KeyboardButton('Bitcoin')
    markup.row(button_a)
    button_b = types.KeyboardButton('Litecoin')
    markup.row(button_b)
    button_c = types.KeyboardButton('Ethereum')
    markup.row(button_c)
    button_d = types.KeyboardButton('Tether')
    markup.row(button_d)
    button_e = types.KeyboardButton('Rub')
    markup.row(button_e)

    bot.send_message(message.chat.id, 'Введите валюту, которую вы хотите обменять.', reply_markup=markup)
    bot.register_next_step_handler(message, on_click, USER_ID)

def question_2(message, USER_ID):
    

    markup = types.ReplyKeyboardMarkup()

    button_a = types.KeyboardButton('Bitcoin')
    markup.row(button_a)
    button_b = types.KeyboardButton('Litecoin')
    markup.row(button_b)
    button_c = types.KeyboardButton('Ethereum')
    markup.row(button_c)
    button_d = types.KeyboardButton('Tether')
    markup.row(button_d)
    button_e = types.KeyboardButton('Rub')
    markup.row(button_e)
   
    bot.send_message(message.chat.id, 'Введите валюту, которую хотите получить.', reply_markup=markup)





     
def enter_number(message, USER_ID):
     global my_number
     global answers
     my_number[USER_ID] = message.text
     answers[USER_ID] += 'Сумма для обмена: '
     answers[USER_ID] += str(my_number[USER_ID])
     answers[USER_ID] += '.\n'
     bot.send_message(message.chat.id, answers[USER_ID])
     
     markup = types.ReplyKeyboardMarkup()

     button_a = types.KeyboardButton('Да')
     markup.row(button_a)
     button_b = types.KeyboardButton('Нет')
     markup.row(button_b)

     bot.send_message(message.chat.id, 'Верно?', reply_markup=markup)

     bot.register_next_step_handler(message, on_clickf, USER_ID)
     
def on_clickf(message, USER_ID):
     if message.text == 'Да':
          bot.send_message(message.chat.id, 'Ожидайте.')
          bot.forward_message(ADMIN, message.chat.id, message.message_id-2)
          user_messages[message.message_id-2] = message.chat.id
          bot.send_message(message.chat.id, message.message_id-2)
          #bot.send_message(ADMIN, user_messages.get(message.message_id))
     elif message.text == 'Нет':
          bot.register_next_step_handler(message, start)


@bot.message_handler(commands=['start'])
def start(message):
     # реализация встроеной бд с очисткой данных при переполнении
     i = 0
     for i in range(LIST-1):
        if USERS[i] == ' ':
             USERS[i] = message.chat.id
             USER_ID = i
             break
        if i == (LIST-1):
             USERS[i] = ' '
             answers[i] = ' '
             my_name[i] = ' '
             my_number[i] = ' '
             break
     bot.send_message(message.chat.id, "Введите данные.")
     question_1(message, USER_ID)
     
@bot.message_handler(func=lambda message: message.chat.id == ADMIN, content_types=['text'])
def handle_response(message):
    # Получаем идентификатор пользователя из словаря
    user_id = user_messages.get(message.reply_to_message.message_id)
    
    #if user_id:
        # Отправляем ответ обратно пользователю
    repl = message.text
    bot.send_message(message.chat.id, message.message_id)
    bot.send_message(ADMIN, f'us {user_id}')
     
     
bot.infinity_polling(timeout=10, long_polling_timeout = 5)






   