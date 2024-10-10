import telebot
bot = telebot.TeleBot("7013766348:AAGkqs_J_593llOnS_ZZ6F4BW5kndA7T_rr8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	message.text = ("salom")
	bot.reply_to(message, message.text)

bot.infinity_polling()