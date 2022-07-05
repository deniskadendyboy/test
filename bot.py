import telebot;
from telebot import types
bot = telebot.TeleBot('%5417066795:AAFHVEO_0BtTnH6xaO33iwZcFihs1_wnloo%');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
if message.text == "text":
    bot.send_message(message.from_user.id, "text")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "text")
else:
    bot.send_message(message.from_user.id, "text /help.")
bot.polling(none_stop=True, interval=0)

keyboard = types.InlineKeyboardMarkup(); 
      key_yes = types.InlineKeyboardButton(text='text', callback_data='yes');
      keyboard.add(key_yes); 
      key_no= types.InlineKeyboardButton(text='text', callback_data='no');
      keyboard.add(key_no);

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": 
        bot.send_message(call.message.chat.id, 'text : )');
    elif call.data == "no":
