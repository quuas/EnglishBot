# English_Bot

Telegram-бот для тестирования уровня английского языка и перевода текста.

## Функционал
- **Тестирование знаний:** Пользователь отвечает на вопросы, чтобы определить уровень владения английским.
- **Перевод текста:** Возможность переводить текст на английский.

## Как запустить
1. Установите Python 3.7 или выше. (Тестировался на Python 3.8)
2. Установите зависимости:
pip install -r requirements.txt
3. Замените `TOKEN` в `telegram_bot.py` на токен вашего бота.
4. Запустите бота:
python telegram_bot.py

## Используемые библиотеки
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [googletrans](https://github.com/ssut/py-googletrans)
- [langdetect](https://pypi.org/project/langdetect/)
