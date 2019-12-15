# -*- coding: utf-8 -*-
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import dialogflow_v2 as dialogflow

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_BOT = os.getenv('TOKEN_BOT')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')


def start(bot, update):
    update.message.reply_text('Здравствуйте! Чем можем помочь?')


def echo(bot, update):
    update.message.reply_text(update.message.text)


def dialog(bot, update):
    client = dialogflow.SessionsClient()
    config = get_file(GOOGLE_APPLICATION_CREDENTIALS)
    session_id = update.message.chat.id

    session = client.session_path(config['project_id'], session_id)
    language_code = update.message.from_user.language_code

    text_input = dialogflow.types.TextInput(
        text=update.message.text,
        language_code=language_code
    )
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = client.detect_intent(
        session=session,
        query_input=query_input
    )

    update.message.reply_text(response.query_result.fulfillment_text)


def get_file(filename: str):
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    updater = Updater(TOKEN_BOT)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, dialog))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
