import telebot
from telebot import types
from googletrans import Translator
from langdetect import detect

TOKEN = 'ВАШ ТОКЕН'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

translator = Translator()

# Объект для хранения ответов пользователя
user_answers = {}

# Словарь для хранения статистики пользователя
user_statistics = {}

# Флаг для отслеживания режима переводчика
is_translator_mode = {}

# Вопросы теста
questions = [
    "1. Выберите вариант, который больше всего подходит для продолжения диалога:\nWhat do you do?\n1) I am an IT-specialist.\n2) We’re cooking pasta.\n3) I hang out with my friends every day.",
    "2. Выберите вариант, который больше всего подходит для продолжения диалога:\nShall we go to the cinema now?\n1) Not at all.\n2) It’s very good.\n3) I’m too tired.",
    "3. Выберите вариант, который больше всего подходит для продолжения диалога:\nHave you ever been abroad?\n1) Sure.\n2) I doubt that.\n3) I think I can.",
    "4. Выберите вариант, который больше всего подходит для продолжения диалога:\nTom and Mary broke up yesterday.\n1) Help yourself.\n2) Such a pity.\n3) I hope I’ll cope with it.",
    "5. Выберите вариант, который больше всего подходит для продолжения диалога:\nI think it’s none of your business!\n1) I’m afraid we have to go.\n2) I beg to differ.\n3) You seem to be lying.",
    "6. Вставьте пропущенное слово: I can’t go out today because I need to look _____ my younger sister.\n1) for\n2) at\n3) after\n4) back",
    "7. Вставьте пропущенное слово: Look! She ______ the fence green.\n1) paint\n2) is painting\n3) are painting\n4) paints",
    "8. Вставьте пропущенное слово:\nHe is coming back from the US ___ next Thursday.\n1) on\n2) in\n3) at\n4) -",
    "9. Вставьте пропущенное слово:\nI’m bored. Can you ____ me some interesting story?\n1) talk\n2) say\n3) speak\n4) tell",
    "10. Вставьте пропущенное слово:\nThey arrived at 7 p.m., opened the door and shouted: “Good _________!”\n1) bye\n2) evening\n3) night\n4) morning",
    "11. Вставьте пропущенное слово:\nHe is such a _______ student that I’m sure he will easily get into the university of his choice.\n1) dynamic\n2) generous\n3) diligent\n4) humble",
    "12. Вставьте пропущенное слово:\n350$??? That’s way ____ expensive for a pair of shoes! I can’t afford it!\n1) enough\n2) too\n3) so\n4) very",
    "13. Вставьте пропущенное слово:\nThey’ve been married for over fifteen years, but she still remembers the day she first _____.\n1) wed him\n2) fell for him\n3) stuck on him\n4) keen on him",
    "14. Выберите правильный вариант:\nI _____ been hit by a car, but luckily I managed to get out of the way.\n1) must have\n2) should have\n3) can have\n4) could have",
    "15. Выберите правильный вариант:\nI wouldn’t take that job if I ____ you.\n1) was\n2) were\n3) would be\n4) am",
    "16. Выберите правильный вариант:\nThis film ______ by Quentin Tarantino.\n1) was directed\n2) is directed\n3) directed\n4) did directed",
    "17. Выберите правильный вариант:\nWe were looking forward _______ our besties after the party to spill some tea!\n1) to see\n2) with seeing\n3) to seeing\n4) to meet",
    "18. Выберите правильный вариант:\nHe hasn’t _____ a decision yet.\n1) done\n2) made\n3) thought\n4) make",
    "19. Выберите правильный вариант:\nCan you tell me ____ ?\n1) is where the coffee shop\n2) where is the coffee shop\n3) the coffee shop is where\n4) where the coffee shop is",
    "20. Выберите правильный вариант:\nThis old-fashioned room design needs _____ .\n1) renovating\n2) to be renovated\n3) being renovated\n4) to be renovating",
    "21. Перефразируйте фразу так, чтобы смысл остался тот же: I don’t mind if you open the window.\n1) I don’t want you to open the window.\n2) It’s fine if you open the window.\n3) It’s better to open the window.",
    "22. Перефразируйте фразу так, чтобы смысл остался тот же: She was keen on pop when she was a child but now she’s more into rock.\n1) She was used to being keen on pop when she was a child but now she’s more into rock.\n2) She got used to being keen on pop when she was a child but now she’s more into rock.\n3) She used to be keen on pop when she was a child but now she’s more into rock.",
    "23. Перефразируйте фразу так, чтобы смысл остался тот же: I’ve been to the hairdresser’s today, so now I have a new hairstyle.\n1) I’ve had my hair cut.\n2) I’ve cut my hair.\n3) I’ve restyled my hair.",
    "24. Перефразируйте фразу так, чтобы смысл остался тот же: I don’t really want to go out tonigh.\n1) I’d better not go out tonight.\n2) I’d rather not go out tonight.\n3) I prefer not go out tonight.",
    "25. Перефразируйте фразу так, чтобы смысл остался тот же: You didn’t ask her out because you are a wallflower.\n1) If you weren’t a wallflower, you would have asked her out.\n2) If you aren’t a walflower, you will ask her out.\n3) If you hadn’t been a walflower, you would have asked her out."
]

# Варианты ответов для каждого вопроса
answer_options = [
    ["I am an IT-specialist", "We’re cooking pasta", "I hang out with my friends every day"],
    ["Not at all", "It’s very good", "I’m too tired"],
    ["Sure", "I doubt that", "I think I can"],
    ["Help yourself", "Such a pity", "I hope I’ll cope with it"],
    ["I’m afraid we have to go", "I beg to differ", "You seem to be lying"],
    ["for", "at", "after", "back"],
    ["paint", "is painting", "are painting", "paints"],
    ["on", "in", "at", "-"],
    ["talk", "say", "speak", "tell"],
    ["bye", "evening", "night", "morning"],
    ["dynamic", "generous", "diligent", "humble"],
    ["enough", "too", "so", "very"],
    ["wed him", "fell for him", "stuck on him", "keen on him"],
    ["must have", "should have", "can have", "could have"],
    ["was", "were", "would be", "am"],
    ["was directed", "is directed", "directed", "did directed"],
    ["to see", "with seeing", "to seeing", "to meet"],
    ["done", "made", "thought", "make"],
    ["is where the coffee shop", "where is the coffee shop", "the coffee shop is where", "where the coffee shop is"],
    ["renovating", "to be renovated", "being renovated", "to be renovating"],
    ["I don’t want you to open the window", "It’s fine if you open the window", "It’s better to open the window"],
    ["She was used to being keen on pop when she was a child but now she’s more into rock", "She got used to being keen on pop when she was a child but now she’s more into rock", "She used to be keen on pop when she was a child but now she’s more into rock"],
    ["I’ve had my hair cut", "I’ve cut my hair", "I’ve restyled my hair"],
    ["I’d better not go out tonight", "I’d rather not go out tonight", "I prefer not go out tonight"],
    ["If you weren’t a wallflower, you would have asked her out", "If you aren’t a walflower, you will ask her out", "If you hadn’t been a walflower, you would have asked her out"]
]

# Правильные ответы
correct_answers = [
    "I am an IT-specialist",
    "I’m too tired",
    "Sure",
    "Such a pity",
    "I beg to differ",
    "after",
    "is painting",
    "-",
    "tell",
    "evening",
    "diligent",
    "too",
    "fell for him",
    "could have",
    "were",
    "was directed",
    "to seeing",
    "made",
    "where the coffee shop is",
    "renovating",
    "It’s fine if you open the window",
    "She used to be keen on pop when she was a child but now she’s more into rock",
    "I’ve had my hair cut",
    "I’d rather not go out tonight",
    "If you weren’t a wallflower, you would have asked her out"
]

# Создаем объект ReplyKeyboardMarkup для кнопок с уменьшенным размером
keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
test_button = telebot.types.KeyboardButton("Пройти тест")
translate_button = telebot.types.KeyboardButton("Переводчик")
statistics_button = telebot.types.KeyboardButton("Статистика")
keyboard.add(test_button, translate_button, statistics_button)

# Функция для отправки теста пользователю с уменьшенными кнопками
def send_question(message, question_number):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for option in answer_options[question_number]:
        markup.add(telebot.types.KeyboardButton(option))

    bot.send_message(message.chat.id, questions[question_number], reply_markup=markup)

# Функция для отправки начальных кнопок 
def send_start_buttons(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    test_button = telebot.types.KeyboardButton("Пройти тест")
    translate_button = telebot.types.KeyboardButton("Переводчик")
    statistics_button = telebot.types.KeyboardButton("Статистика")
    markup.add(test_button, translate_button, statistics_button)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Функция для отправки статистики пользователю
def send_user_statistics(message, user_id):
    if user_id in user_statistics:
        statistics = user_statistics[user_id]
        bot.send_message(message.chat.id, f"Ваша статистика:\nВсего тестов: {statistics['total_tests']}\nПравильных ответов: {statistics['correct_answers']}\nУровень владения английским: {statistics['language_level']}")
    else:
        bot.send_message(message.chat.id, "У вас пока нет статистики.")

# Функция для сброса статистики пользователя
def reset_user_statistics(message, user_id):
    if user_id in user_statistics:
        user_statistics[user_id] = {"total_tests": 0, "correct_answers": 0, "language_level": "Beginner"}
        bot.send_message(message.chat.id, "Статистика сброшена.")
    else:
        bot.send_message(message.chat.id, "У вас пока нет статистики.")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    if user_id not in user_answers:
        user_answers[user_id] = {"score": 0, "question_number": 0}
    if user_id not in is_translator_mode:
        is_translator_mode[user_id] = False
    if user_id not in user_statistics:
        user_statistics[user_id] = {"total_tests": 0, "correct_answers": 0, "language_level": "Beginner"}

    bot.send_message(message.chat.id, "Привет! welcome в чат-бот для изучения английского языка. Здесь вы можете пройти тест на уровень владения языком, посмотреть статистику ваших результатов или воспользоваться переводчиком.",
                    reply_markup=keyboard)

# Обработчик кнопки "Пройти тест"
@bot.message_handler(func=lambda message: message.text == "Пройти тест")
def handle_start_buttons(message):
    if message.text == "Пройти тест":
        bot.send_message(message.chat.id, "Hi there! Вы собираетесь пройти тест на определение уровня английского языка. Этот тест содержит 25 вопросов: какие-то из них проще, какие-то сложнее - поэтому не расстраивайтесь, если вы чего-то не знаете или забыли! Во время прохождения теста не подглядывайте и не гуглите ответы - идея в том, чтобы определить ваш приблизительный уровень на данный момент! Готовы пройти? (Да/Нет)")

# Обработчик кнопки "Переводчик"
@bot.message_handler(func=lambda message: message.text == "Переводчик")
def handle_translate_button(message):
    user_id = message.from_user.id
    is_translator_mode[user_id] = True
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    return_button = telebot.types.KeyboardButton("Вернуться назад")
    markup.add(return_button)
    bot.send_message(message.chat.id, "Введите текст для перевода", reply_markup=markup)

# Обработчик текстовых сообщений для перевода
@bot.message_handler(func=lambda message: is_translator_mode.get(message.from_user.id, False) and message.content_type == 'text')
def handle_translation(message):
    user_id = message.from_user.id
    text_to_translate = message.text
    
    if text_to_translate == 'Вернуться назад':
        is_translator_mode[user_id] = False
        bot.send_message(message.chat.id, "Вы вышли из режима переводчика.")
        send_start_buttons(message)
    else:
        translated_text = translator.translate(text_to_translate, dest='en').text
        bot.send_message(message.chat.id, translated_text)

# Обработчик кнопки "Статистика"
@bot.message_handler(func=lambda message: message.text == "Статистика")
def handle_statistics_button(message):
    user_id = message.from_user.id
    send_user_statistics(message, user_id)

    # Добавим кнопки "Сбросить статистику" и "Вернуться назад"
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    reset_stats_button = telebot.types.KeyboardButton("Сбросить статистику")
    back_button = telebot.types.KeyboardButton("Вернуться назад")
    markup.add(reset_stats_button, back_button)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработчик кнопки "Сбросить статистику"
@bot.message_handler(func=lambda message: message.text == "Сбросить статистику")
def handle_reset_stats_button(message):
    user_id = message.from_user.id
    reset_user_statistics(message, user_id)
    send_start_buttons(message)

# Обработчик кнопки "Вернуться назад"
@bot.message_handler(func=lambda message: message.text.lower() == "вернуться назад")
def handle_back_button(message):
    send_start_buttons(message)

# Обработчик ответа на начало теста
@bot.message_handler(func=lambda message: message.text.lower() in ['да', 'нет'])
def handle_test_begin(message):
    user_id = message.from_user.id
    if message.text.lower() == 'да':
        user_statistics[user_id]["total_tests"] += 1
        user_answers[user_id] = {"score": 0, "question_number": 0}
        send_question(message, 0)
    else:
        send_start_buttons(message)

# Обработчик ответов на вопросы теста
@bot.message_handler(func=lambda message: not is_translator_mode.get(message.from_user.id, False) and message.content_type == 'text')
def handle_test_answers(message):
    user_id = message.from_user.id

    if user_id in user_answers:
        # Проверяем ответ пользователя
        current_question = user_answers[user_id]["question_number"]
        if message.text == correct_answers[current_question]:
            user_answers[user_id]["score"] += 1
            user_statistics[user_id]["correct_answers"] += 1

        # Переходим к следующему вопросу или завершаем тест
        user_answers[user_id]["question_number"] += 1
        if user_answers[user_id]["question_number"] < len(questions):
            send_question(message, user_answers[user_id]["question_number"])
        else:
            # Определяем уровень владения языком
            score = user_answers[user_id]["score"]
            level = None
            score = user_answers[user_id]["score"]
            if score == 0:
                level = "Beginner."
            elif score <= 5:
                level = "Elementary."
            elif score <= 10:
                level = "Pre-Intermediate."
            elif score <= 15:
                level = "Intermediate."
            elif score <= 20:
                level = "Upper-Intermediate."
            else:
                level = "Advanced."
                    
            user_statistics[user_id]["language_level"] = level
            bot.send_message(message.chat.id, f"Тест пройден! Ваш приблизительный уровень - {level} Вы можете посмотреть свой результат перейдя в статистику.")
            send_start_buttons(message)

# Запускаем бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
