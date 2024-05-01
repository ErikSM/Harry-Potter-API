import json
import requests


def create_generator(data_list: list):
    for i in data_list:
        yield i


def make_request(complement, research=''):
    address = "https://hp-api.onrender.com/api/"
    text = ''

    if complement == "all characters":
        text = "characters"
    elif complement == "specific character":
        text = f"character/{research}"
    elif complement == "hogwarts students":
        text = "characters/students"
    elif complement == "hogwarts staff":
        text = "characters/staff"
    elif complement == 'houses':
        text = f"characters/house/{research}"
    elif complement == 'spells':
        text = 'spells'

    try:
        request = requests.get(f"{address}{text}")
        list_required = json.loads(request.text)

    except Exception as ex:
        list_required = [{'Error': f"{ex}", 'search': f"{complement}", 'address': f"{address}"}]

    return list_required
