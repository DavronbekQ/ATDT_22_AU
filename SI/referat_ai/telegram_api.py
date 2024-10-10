import telebot
from ai_surov import ai_surov
from doc_creator import doc_creator

bot = telebot.TeleBot("6714544648:AAGEp3tv_H4fd5mETPF2_cVCYn0uYmFec_8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Raferat mavzusini kiriting")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print(message.text)
	bot.reply_to(message, message.text)

bot.infinity_polling()