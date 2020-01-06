import json
from random import randint

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

import dialogflow_v2 as dialogflow

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_VK = os.environ.get('TOKEN_VK')
GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')


def handle_message(event, vk_api):
    client = dialogflow.SessionsClient()

    with open(GOOGLE_APPLICATION_CREDENTIALS, 'r') as file:
        config = json.load(file)

    session = client.session_path(config['project_id'], event.user_id)
    text_input = dialogflow.types.TextInput(
        text=event.text,
        language_code='ru'
    )
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = client.detect_intent(
        session=session,
        query_input=query_input
    )

    if response.query_result.intent.display_name:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response.query_result.fulfillment_text,
            random_id=randint(1, 1000)
        )


if __name__ == "__main__":
    vk_session = vk_api.VkApi(token=TOKEN_VK)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handle_message(event, vk_api)
