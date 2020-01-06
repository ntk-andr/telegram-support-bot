import json

import dialogflow_v2 as dialogflow
from google.api_core.exceptions import FailedPrecondition
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')


def create_intents():
    client = dialogflow.IntentsClient()
    with open(GOOGLE_APPLICATION_CREDENTIALS, 'r') as configfile:
        config = json.load(configfile)

    parent = client.project_agent_path(config['project_id'])

    with open('intents.json', 'r') as intentsfile:
        intents = json.load(intentsfile)

    for intent in intents:
        try:
            client.create_intent(parent, intent)
        except FailedPrecondition:
            continue


if __name__ == '__main__':
    create_intents()
