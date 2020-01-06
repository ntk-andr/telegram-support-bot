# Бот помощник Telegram и VK
Cоздан для закрытия типичных вопросов службы поддержки.

## для запуска требуется
- Python 3.6 и выше
- Установить зависимости командой `pip install -r requirements.txt`
- Создать файл .env в корне проекта с переменными: 
     `TOKEN_BOT`, `GOOGLE_APPLICATION_CREDENTIALS`, `TOKEN_VK`
    
    пример:

        TOKEN_BOT=1233435
        GOOGLE_APPLICATION_CREDENTIALS=path/to/file.json
        TOKEN_VK=111222333

- Запустить командой `python bot.py`

## Выгрузка на Heroku
- Регистрируемся
- Добавляем новое приложение
- Соединяем с репозиторием
- В разделе Settings -> Config Vars добавляем переменные окружения
    
    Для переменной `GOOGLE_APPLICATION_CREDENTIALS` делаем как показано ниже  
    ![Alt Text](https://i.stack.imgur.com/3gxMn.png)
    `GOOGLE_CREDENTIALS` - путь до файла JSON
    `GOOGLE_APPLICATION_CREDENTIALS` - содержимое файла JSON
- В терминале пишем: `heroku buildpacks:add https://github.com/elishaterada/heroku-google-application-credentials-buildpack -a APP` 
    где APP имя нашего приложения 
- В разделе Resources активируем выполнение команды bot: python3 bot.py

> Чтобы создать JSON-ключ идем сюда https://cloud.google.com/docs/authentication/getting-started

### Результат:

Telegram:

![Telegram](https://dvmn.org/filer/canonical/1569214094/323/)

---
Vk: 

![Vk](https://dvmn.org/filer/canonical/1569214089/322/)