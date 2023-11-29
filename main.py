import telebot

bot = telebot.TeleBot('6733986740:AAHjmmcdlyH_a_HjwkYkbZWDMGqudDv4m3I')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Привет!* Что выберешь? Кошек 🐱 или ëжиков 🦔? \n Пиши /cats или /hedgehogs',
                     parse_mode='Markdown')


@bot.message_handler(commands=['cats'])
def main(message):
    bot.send_message(message.chat.id,
                     'Отличный выбор! [Тыкай сюда] (https://ru.wallpaper.mob.org/gallery/tag=oshki_oty_otiki/)',
                     parse_mode='markdown')


@bot.message_handler(commands=['hedgehogs'])
def main(message):
    bot.send_message(message.chat.id, 'Отличный выбор! [Тыкай сюда] (https://ru.wallpaper.mob.org/gallery/tag=ezhiki/)',
                     parse_mode='markdown')


bot.infinity_polling()