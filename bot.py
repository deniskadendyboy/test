import telebot;
from telebot import types
bot = telebot.TeleBot('%5417066795:AAFHVEO_0BtTnH6xaO33iwZcFihs1_wnloo%');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
if message.text == "текст сообщения":
    bot.send_message(message.from_user.id, "реакция на сообщение")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши команду")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)

keyboard = types.InlineKeyboardMarkup(); #клавиатура
      key_yes = types.InlineKeyboardButton(text='кнопка', callback_data='yes');
      keyboard.add(key_yes); 
      key_no= types.InlineKeyboardButton(text='кнопка', callback_data='no');
      keyboard.add(key_no);

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": 
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
