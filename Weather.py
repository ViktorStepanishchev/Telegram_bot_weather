import telebot
import webbrowser
import time
import requests
from telebot import types
import json

API = ''

markup_keyboard = types.ReplyKeyboardMarkup()
btn1_k = types.KeyboardButton('Узнать погоду от бота 🤖')
markup_keyboard.row(btn1_k)
btn2_k = types.KeyboardButton('Узнать погоду на сайте 🌐')
btn3_k = types.KeyboardButton('Нужна помощь ⚙')
markup_keyboard.row(btn2_k, btn3_k)

bot = telebot.TeleBot(open("bot.txt").readline().strip())

@bot.message_handler(content_types=["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"])
def get_file(message):
    bot.reply_to(message, 'Нееее, моя задача говорить погоду, если хотите узнать погоду - пишите /start', reply_markup=markup_keyboard)

@bot.message_handler(commands=['сайт', 'site'])
def site(message):
    bot.send_message(message.chat.id, 'Сейчас перенаправим вас на сайт, если вы с компьютера 🖥. Если же Вы пользуетесь мобильным телефоном, то откройте ссылку самостоятельно 📱')
    bot.send_message(message.chat.id, 'https://yandex.ru/pogoda/moscow?from=1&lat=55.755863&lon=37.6177')
    time.sleep(2.5)
    webbrowser.open('https://yandex.ru/pogoda/moscow?from=1&lat=55.755863&lon=37.6177')

@bot.message_handler(commands=['начать', 'start'])
def main(message):
    username = str(message.from_user.first_name)
    bot.send_message(message.chat.id, f'👋 Здравствуйте, {username}, напишите город, в котором хотите узнать погоду! 🏙', reply_markup=markup_keyboard)

@bot.message_handler()
def info(message):
    username = str(message.from_user.first_name)
    if message.text == 'Узнать погоду от бота 🤖':
        username = str(message.from_user.first_name)
        bot.send_message(message.chat.id, f'👋 Здравствуйте, {username}, напишите город, в котором хотите узнать погоду! 🏙', reply_markup=markup_keyboard)                                  # импорт погоды в мск
    elif message.text == 'Узнать погоду на сайте 🌐':
        bot.send_message(message.chat.id, 'Сейчас перенаправим вас на сайт, если вы с компьютера 🖥. Если же Вы пользуетесь мобильным телефоном, то откройте ссылку самостоятельно 📱')
        bot.send_message(message.chat.id, 'https://yandex.ru/pogoda/moscow?from=1&lat=55.755863&lon=37.6177')
        time.sleep(2.5)
        webbrowser.open('https://yandex.ru/pogoda/moscow?from=1&lat=55.755863&lon=37.6177')
    elif message.text == "Нужна помощь ⚙":
         bot.send_message(message.chat.id, 'Используйте кнопки на вашей клавиатуре смартфона/компьютера ⌨')
         bot.send_message(message.chat.id, 'Если вы разобрались с клавиатурой на вашем дивайсе, то просто напишите название города, в котором хотите узнать погоду 🏙')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Здравствуйте, {username}, просто напишите название Вашего города, чтобы я подсказал погоду 🙄', reply_markup=markup_keyboard)
    elif message.text.lower() == 'пидор':
        bot.send_message(message.chat.id, 'Пошел нахуй, кожаный выблядок', reply_markup=markup_keyboard)
    elif message.text.lower() == 'долбоеб':
        bot.send_message(message.chat.id, 'Ты как базаришь, помет хуеглазый', reply_markup=markup_keyboard)
    elif message.text.lower() == 'хуесос':
        bot.send_message(message.chat.id, 'Соси, слоняра таёжная', reply_markup=markup_keyboard)
    elif message.text.lower() == 'иди нахуй':
        bot.send_message(message.chat.id, 'Сам иди, пидор чумазый', reply_markup=markup_keyboard)
    elif message.text.lower() == 'пошел нахуй':
        bot.send_message(message.chat.id, 'Сам иди, пидор чумазый', reply_markup=markup_keyboard)
    else:
        city1 = message.text.strip()
        city = message.text.strip().lower()
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        if res.status_code == 200:
            data = json.loads(res.text)
            temp = str(int(data["main"]["temp"]))
            feels = str(int(data["main"]["feels_like"]))
            bot.send_message(message.chat.id, f'Выбранный Вами город: {city1} 🌃, ищем информацию по нему  🔍')
            bot.reply_to(message, '🌡 Погода в выбранном городе: ' + temp + ' °C')
            bot.send_message(message.chat.id, '🧘 Ощущается ‍как '+ feels + ' °C', reply_markup=markup_keyboard)
        else:
            bot.reply_to(message, 'Вы указали несуществующий город, либо его нет в базе данных 😔')


bot.polling(none_stop=True)
























