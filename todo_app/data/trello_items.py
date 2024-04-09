import json
import os
import dotenv
import requests

from todo_app.data.item import Item

dotenv.load_dotenv()
key = os.getenv('TRELLO_API_KEY')
token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')
to_do_list_id = os.getenv('TRELLO_TO_DO_LIST_ID')
doing_list_id = os.getenv('TRELLO_DOING_LIST_ID')
done_list_id = os.getenv('TRELLO_DONE_LIST_ID')

def get_items():
    url = f"https://api.trello.com/1/boards/{board_id}/lists"

    headers = {
    "Accept": "*/*"
    }

    query = {
    'key': key,
    'token': token,
    'cards': 'open',
    }

    response = requests.get(
    url,
    headers=headers,
    params=query
    )

    response.raise_for_status()

    response_json = response.json()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            item = Item.from_trello_card(card, trello_list)
            cards.append(item)

    return cards

def add_item(title):
    url = "https://api.trello.com/1/cards"

    headers = {
    "Accept": "*/*"
    }

    query = {
    'idList': to_do_list_id,
    'key': key,
    'token': token,
    'name': title
    }

    response = requests.post(
    url,
    headers=headers,
    params=query,

    )

    print(response.text)

def update_status_to_done(itemId):
    url = f"https://api.trello.com/1/cards/{itemId}"

    headers = {
    "Accept": "*/*"
    }

    query = {
    'key': key,
    'token': token,
    'idList': done_list_id

    }

    response = requests.put(
    url,
    headers=headers,
    params=query
    )

