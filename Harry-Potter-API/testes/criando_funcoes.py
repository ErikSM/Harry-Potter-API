import json
import requests
from api_config.configuration import movies_colors, id_sample
from api_config.data_api import hogwarts_houses_students

book_colors = movies_colors
id_sample = id_sample


def request_testing(complement, research=''):
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
        dict_required = json.loads(request.text)

    except Exception as ex:
        dict_required = {'docs': [{'name': 'Error on request', '_id': f'{ex}'}], 'total': 'xx',
                         'limit': 'xx', 'offset': 'xx', 'page': 'xx', 'pages': 'xx'}

    return dict_required


def characters_testing(search=None):
    all_characters = request_testing('all characters')

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

    print(len(all_characters))


def specific_character_testing(id_code):
    id_code = id_code
    specific = request_testing('specific character', id_code)

    for i in specific:
        for j in i:
            print(f"{j}: {i[j]}")

        print(len(i))


def students_testing():
    students = request_testing('hogwarts students')

    for i in students:
        print(i)
    print(len(students))


def staffs_testing():
    all_staffs = request_testing("hogwarts staff")

    for i in all_staffs:
        print(i)
    print(len(all_staffs))


def houses_testing():
    all_houses = dict()
    for i in hogwarts_houses_students:
        all_houses[i] = request_testing("houses", hogwarts_houses_students[i])

    for i in all_houses:
        print(f"-{i}: ({len(all_houses[i])} students)")


def spells_testing():
    spells = request_testing('spells')

    for i in spells:
        print(i)


#  -----------------------------------------------------------


def all_species_testing():
    all_characters = request_testing('all characters')
    species = set()

    for i in all_characters:
        for j in i:
            if j == 'species':
                species.add(i[j])
    for i in species:
        print(i)


def date_of_birth_testing():
    all_characters = request_testing('all characters')

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


def ancestry_testing():
    all_characters = request_testing('all characters')
    ancestry = set()

    for i in all_characters:
        for j in i:
            if j == 'ancestry':
                if i[j] == '':
                    ancestry.add('None')
                else:
                    ancestry.add(i[j])

    for i in ancestry:
        print(i)


def actors_testing():
    all_characters = request_testing('all characters')

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
                else:
                    alternative = 'xxx'

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


#  --------------------------------------------


def all_characters_keys_testing():
    all_characters = request_testing('all characters')
    all_keys = set()

    for i in all_characters:
        for j in i:
            all_keys.add(j)

    for i in all_keys:
        print(i)


def boolean_keys_testing():
    all_characters = request_testing('all characters')

    boolean_keys = set()
    for i in all_characters:
        for j in i:
            if i[j] == bool():
                boolean_keys.add(j)

    for i in boolean_keys:
        print(i)
    print(f"total: {len(boolean_keys)}")


def image_testing():
    all_characters = request_testing('all characters')

    images = list()
    for i in all_characters:
        for j in i:
            if j == 'image':
                if i[j] == '':
                    pass
                else:
                    images.append(i[j])

    print(len(images))
    for i in images:
        print(i)


staffs_testing()

