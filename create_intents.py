import json

import dialogflow_v2 as dialogflow
from google.api_core.exceptions import FailedPrecondition
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')


def get_file(filename: str):
    with open(filename, 'r') as file:
        return json.load(file)


def create_intents():
    client = dialogflow.IntentsClient()
    config = get_file(GOOGLE_APPLICATION_CREDENTIALS)
    parent = client.project_agent_path(config['project_id'])
    intents = get_file('intents.json')
    for intent in intents:
        try:
            client.create_intent(parent, intent)
        except FailedPrecondition:
            continue


if __name__ == '__main__':
    create_intents()
