import json
import requests
from configuration import movies_colors, hogwarts_houses, id_sample


book_colors = movies_colors
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


def characters_testing(search=None):
    all_characters = make_request('all characters')

    for i in all_characters:
        for j in i:
            if j == 'id':
                print(i[j])
            else:
                print(f"{j}: {i[j]}")

        print(len(all_characters))
        print(len(i))

    if search is not None:
        for i in all_characters:
            for j in i:
                if j == 'name':
                    if i[j] == search:
                        print('ok founded')
                        print(f" ### {i[j]}: ({search}) ###")
                    else:
                        pass


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
    house = make_request("houses")
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


def date_of_birth_testing():
    all_characters = make_request('all characters')
    cont_unknown = 0
    cont_know = 0
    name = ''

    for i in all_characters:
        for j in i:
            if j == 'name':
                name = i[j]
            elif j == 'dateOfBirth':
                if i[j] is None:
                    cont_unknown += 1
                else:
                    cont_know += 1
                    print(name)
                    print(f"{j}: {i[j]}")

    print("\n----------------\n")
    print(f'unknown: {cont_unknown}')
    print(f'know: {cont_know}')


def actors_testing():
    all_characters = make_request('all characters')

    cont_unknown = 0
    cont_know = 0

    name = ''
    alternative = 'None'

    for i in all_characters:
        for j in i:
            if j == 'name':
                name = i[j]
            elif j == 'alternate_actors':
                if len(i[j]) != 0:
                    alternative = i[j]

            elif j == 'actor':
                if i[j] == '':
                    cont_unknown += 1
                else:
                    cont_know += 1
                    print(name)
                    print(f"{j}: {i[j]}")
                    print(f"alternative actor:(( {alternative}))")

    print("\n----------------\n")
    print(f'unknown: {cont_unknown}')
    print(f'know: {cont_know}')




