from api_config.configuration import play_options_and_code, menu_play_and_code
from api_config.data_api import all_characters, houses_names, all_spells, ancestry_names, hogwarts_houses, by_species, \
    by_ancestries, species_names, hogwarts_students, hogwarts_staffs


def processing_play(menu_play_captured):

    options_chosen = list()

    try:
        captured_option_code = menu_play_and_code[menu_play_captured]

    except KeyError as ex:
        error = f"xX!x ErRor ?XxX"
        ex = f"[{ex}] not valid"

        options_chosen.append(error)
        options_chosen.append(ex)

    else:
        for i in play_options_and_code:
            option_got = i[0]
            option_code = i[1]

            if option_code == captured_option_code:
                options_chosen.append(option_got)
            else:
                pass

    finally:
        return options_chosen


def processing_select(selected):

    text_title = f"*{selected}:\n\n\n"
    list_string = list()
    text_string = list()

    if selected == 'Characters':
        for i in all_characters:
            list_string.append(i.name)
            text_string.append(f"- ({i.name}):\n{i.code_id}\n\n")
    elif selected == 'Ids':
        for i in all_characters:
            list_string.append(i.code_id)
            text_string.append(f"- ({i.name}):\n{i.code_id}\n\n")
    elif selected == 'Spells':
        for i in all_spells:
            list_string.append(i['name'])
            text_string.append(f"> {i['name']}:\n-{i['description']}\n\n\n")
    elif selected == 'Students':
        for i in hogwarts_students:
            list_string.append(i['name'])
            text_string.append(f"{i['id']} :\n {i['name']}\n\n")
    elif selected == 'Staffs':
        for i in hogwarts_staffs:
            list_string.append(i['name'])
            text_string.append(f"{i['id']} :\n {i['name']}\n\n")
    elif selected == 'Houses':
        for i in hogwarts_houses:
            list_string.append(i)
            text_string.append(f"{i}: {len(hogwarts_houses[i])} students")
            text_string.append(f'\n')
            text_string.append(f'\n')
    elif selected == 'Species':
        for i in by_species:
            list_string.append(i)
            text_string.append(f"{i}: {len(by_species[i])} characters\n\n")
    elif selected == "Date of Birth":
        for i in all_characters:
            list_string.append(i.name)
            text_string.append(f"{i.name}: {i.birth}\n\n")
    elif selected == 'Ancestry':
        for i in by_ancestries:
            list_string.append(i)
            text_string.append(f"{i}: {len(by_ancestries[i])} characters\n\n")
    elif selected == 'Actors':
        for i in all_characters:
            if i.actor != '':
                list_string.append(i.actor)
                text_string.append(f"{i.actor}: {i.name}\n\n")
    else:
        error = 'Xx?1 ErROr XxX7\n\n'
        list_string, text_title, text_string = [error], error, [error]

    return list_string, text_title, text_string


def processing_item(selected, item):

    for i in play_options_and_code:
        if i[0] == selected:
            continue
        else:
            pass

    title = f'*{selected}: ({item})\n\n\n'
    text_list = list()

    if selected == 'Characters':
        for i in all_characters:
            if item == i.name:

                info = i.all_info()
                for j in info:
                    text_list.append(f'{j}\n')

    if selected == 'Ids':
        for i in all_characters:
            if item == i.code_id:

                info = i.all_info()
                for j in info:
                    text_list.append(f'{j}\n')

    if selected == 'Spells':
        for i in all_spells:
            if item == i['name']:

                info = i
                for j in info:
                    text_list.append(f'- {j} : \n{info[j]}\n\n')

    if selected == 'Students':
        for i in hogwarts_students:
            if item == i['name']:

                info = i
                for j in info:
                    text_list.append(f'{j} :  {info[j]}\n')

    if selected == 'Staffs':
        for i in hogwarts_staffs:
            if item == i['name']:

                info = i
                for j in info:
                    text_list.append(f'{j} :  {info[j]}\n')

    if selected == 'Houses':
        for i in hogwarts_houses:
            if item == i:

                info = hogwarts_houses[i]
                for j in info:
                    text_list.append(f' {j["id"]} :  \n- {j["name"]}\n\n')

    if selected == 'Date of Birth':
        for i in all_characters:
            if item == i.name:

                if i.alive:
                    status = 'alive'
                else:
                    status = 'dead'
                text_list.append(f'{i.name}: {i.birth}\n({status})\n')

    if selected == 'Ancestry':
        for i in by_ancestries:
            if item == i:

                info = by_ancestries[i]
                for j in info:
                    text_list.append(f'name: {j[0]}\nid: {j[1]}\n\n')

    if selected == 'Species':
        for i in by_species:
            if item == i:

                info = by_species[i]
                for j in info:
                    text_list.append(f'name: {j[0]}\nid: {j[1]}\n\n')

    if selected == 'Actors':
        for i in all_characters:
            if item == i.actor:

                if i.actor != '':
                    text_list.append(f'- Character: {i.name}\nActor: {i.actor}\nId: {i.code_id}\n\n')

    return title, text_list


def processing_search(improve, improve_research_enabled, word_captured):
    characters = all_characters
    spells = all_spells
    houses = houses_names
    species = species_names
    ancestries = ancestry_names

    character_name = ''
    actor_name = ''
    house_name = ''
    spell_name = ''
    specie_name = ''
    ancestry_type = ''
    id_number = ''

    type_found = "Not found"
    to_print = "Not found"

    details_info = 'Not Found'

    founded = False

    a_character = False
    a_actor = False
    a_house = False
    a_spell = False
    a_specie = False
    a_ancestry = False
    a_id = False

    if not improve_research_enabled or improve == 'character':
        for i in characters:
            if i.name.title() == word_captured.title():
                founded = True
                a_character = True
                character_name = i.name
                type_found = "character"

                details_info = i.all_info()

            if i.actor == word_captured:
                founded = True
                a_actor = True
                actor_name = i.actor
                type_found = "actor"

                details_info = i.all_info()

    if not improve_research_enabled or improve == 'house':
        for i in houses:
            if i.title() == word_captured.title():
                founded = True
                a_house = True
                house_name = i
                type_found = "house"

                details_info = [f"House:{i.title()}\n", f" -{len(hogwarts_houses[i.title()])} students"]

    if not improve_research_enabled or improve == 'spell':
        for i in spells:
            for j in i:
                if j == 'name':
                    if i[j].title() == word_captured.title():
                        founded = True
                        a_spell = True
                        spell_name = i[j]
                        type_found = "spell"

                        info = i
                        details_info = [f'({z}): \n  - {info[z]}' for z in info]

    if not improve_research_enabled or improve == 'specie':
        for i in species:
            if i.title() == word_captured.title():
                founded = True
                a_specie = True
                specie_name = i
                type_found = 'specie'

                details_info = [f"*Name: {i[0].title()} \nid:{i[1]}" for i in by_species[i]]

    if not improve_research_enabled or improve == 'ancestry':
        for i in ancestries:
            if i.title() == word_captured.title():
                founded = True
                a_ancestry = True
                ancestry_type = i
                type_found = 'ancestry'

                details_info = [f"*Name: {i[0].title()} \nid:{i[1]}" for i in by_ancestries[i]]

    if not improve_research_enabled or improve == 'id':
        for i in all_characters:
            if i.code_id == word_captured:
                founded = True
                a_id = True
                id_number = i.code_id
                type_found = 'Id'

                details_info = i.all_info()

    if founded:
        if a_character:
            to_print = character_name
        elif a_actor:
            to_print = actor_name
        elif a_house:
            to_print = house_name
        elif a_spell:
            to_print = spell_name
        elif a_specie:
            to_print = specie_name
        elif a_ancestry:
            to_print = ancestry_type
        elif a_id:
            to_print = id_number

        was_sought = f"was sought:({word_captured})"

        ok_founded = f"OK founded: {to_print}*"
        type_searched = f"type:[[{type_found}]]"

        result_info = [was_sought, ok_founded, type_searched]
        return result_info, details_info

    else:
        result_info = ['not found']
        details_info = [details_info, "\n[ xxx ]"]
        return result_info, details_info
