import json
import requests
from configuration import book_colors, hogwarts_houses, id_sample


book_colors = book_colors
houses = hogwarts_houses
id_sample = id_sample


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
        text = f"characters/house/{complement}"
    elif complement == 'spells':
        text = 'spells'

    try:
        request = requests.get(f"{address}{text}")
        dict_required = json.loads(request.text)

    except Exception as ex:
        dict_required = {'docs': [{'name': 'Error on request', '_id': f'{ex}'}], 'total': 'xx',
                         'limit': 'xx', 'offset': 'xx', 'page': 'xx', 'pages': 'xx'}

    return dict_required


def characters_testing():
    all_characters = make_request('all characters')
    for i in all_characters:
        for j in i:
            if j == 'id':
                print(i[j])
            else:
                print(f"{j}: {i[j]}")

        print(len(all_characters))
        print(len(i))


def specific_character_testing(id_code):
    id_code = id_code
    specific = make_request('specific character', id_code)
    for i in specific:
        print(i)
        print(len(i))


def staffs_testing():
    all_staffs = make_request("hogwarts staff")
    for i in all_staffs:
        print(i)


def house_testing():
    house = make_request("house")
    for i in house:
        print(i)


def spells_testing():
    spells = make_request('spells')
    for i in spells:
        print(i)


def all_species_testing():
    all_characters = make_request('all characters')
    species = set()

    for i in all_characters:
        for j in i:
            if j == 'species':
                species.add(i[j])

    for i in species:
        print(i)


characters_testing()
