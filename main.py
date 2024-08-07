import telebot

bot = telebot.TeleBot("7177238465:AAHVoJOjVmqHpShYiGWA6s5tt4OCcqYbPEk")

@bot.message_handler(commands= ["start"])
def greeting(message):
    if message.from_user.last_name:
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}!")
    else:
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!")

@bot.message_handler(commands=['price'])
def price_handler(message):
    bot.send_message(message.chat.id, "Введи *одну из трёх* ценовых категорий кубиков Рубика 3 на 3: _Бюджетная_, _Среднебюджетная_, _Флагманская_.", parse_mode="Markdown")

@bot.message_handler(commands=['brand'])
def brand_handler(message):
    bot.send_message(message.chat.id, "Введи *один из трёх* наиболее популярных брендов кубиков Рубика 3 на 3: _GAN_, _QiYi_, _MoYu_.", parse_mode="Markdown")

@bot.message_handler(commands=['type'])
def type_handler(message):
    bot.send_message(message.chat.id, "Введи *один из трёх* видов головоломок: _3 на 3_, _4 на 4_, _5 на 5_.", parse_mode="Markdown")

@bot.message_handler(commands=["correct_nickname"])
def checking_correctness(message):
    bot.send_message(message.chat.id, "Введи никнейм вида: _nickname1for1bot - nick_,  бот проверит его на соответствие параметрам: длина имени не более 20 символов, имя не начинается с цифры, имя заканчивается на слово bot (используя стандартные методы строк, без среза).", parse_mode="Markdown")

@bot.message_handler()
def text_mess(message):
    if "gan" in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/3x3/manufacturer_gan/")
    if "qiyi" in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/3x3/manufacturer_qiyi-mofangge/")
    if "moyu" in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/3x3/manufacturer_moyu/")
    if "3 на 3" in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/3x3/")
    if "4 на 4" in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/4x4/")
    if "5 на 5" in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/5x5/")
    if "бюджетная" in message.text.lower() and "среднебюджетная" not in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/3x3/filter/price-base-to-2000/apply/")
    if "среднебюджетная" in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/3x3/filter/price-base-from-2000-to-4000/apply/")
    if "флагманская" in message.text.lower():
        bot.reply_to(message, "https://cccstore.ru/catalog/kubiki-rubika/3x3/filter/price-base-from-4000/apply/")
    if " - nick" in message.text.lower():
        if (len(message.text.lower()[:-7]) <= 20) and (not(message.text.lower()[0].isdigit())) and (message.text.lower()[-10:-7] == "bot"):
            bot.send_message(message.chat.id, "Никнейм корректный")
        else:
            bot.send_message(message.chat.id, "Никнейм некорректный")

bot.infinity_polling()
