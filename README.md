#  Telegram Бот помощник
создан для закрытия типичных вопросов службы поддержки.

## для запуска требуется
- python 3.6 и выше
- установить зависимости командой `pip install -r requirements.txt`
- создать файл .env в корне проекта с переменными: 
    - TOKEN_BOT,
    - GOOGLE_APPLICATION_CREDENTIALS
    
пример:

    TOKEN_BOT=1233435
    GOOGLE_APPLICATION_CREDENTIALS=path/to/file.json

- запустить командой `python bot.py`

## Выгрузка на Heroku
- Регистрируемся
- Добавляем новое приложение
- соединяем с репозиторием
- в разделе Settings -> Config Vars добавляем переменные окружения
    -  для переменной GOOGLE_APPLICATION_CREDENTIALS делаем как показано ниже  
    ![Alt Text](https://i.stack.imgur.com/3gxMn.png)
    > GOOGLE_CREDENTIALS - путь до файла JSON
    > GOOGLE_APPLICATION_CREDENTIALS - содержимое файла JSON
    - в терминале пишем: `heroku buildpacks:add https://github.com/elishaterada/heroku-google-application-credentials-buildpack -a APP` 
    где APP имя нашего приложения 
- в разделе Resources активируем выполнение команды bot: python3 bot.py

> чтобы создать JSON-ключ идем сюда https://cloud.google.com/docs/authentication/getting-started

### Результат:
![Alt Text](https://dvmn.org/filer/canonical/1569214094/323/)