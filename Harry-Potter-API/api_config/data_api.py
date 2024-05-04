from api_config.access import create_generator, make_request
from objects.Character import Character


_characters_requested = create_generator(make_request('all characters'))
_characters_list = list(_characters_requested)
all_characters = list()

_spells_requested = create_generator(make_request('spells'))
all_spells = list(_spells_requested)

houses_names = ["gryffindor", "ravenclaw", "hufflepuff", "slytherin"]
hogwarts_houses = {i.title(): list() for i in houses_names}

ancestry_names = ["muggle", "squib", "half-blood", "quarter-veela", "muggleborn", "pure-blood", "half-veela"]
by_ancestries = {i: list() for i in ancestry_names}

species_names = ["three-headed dog", "centaur", "house-elf", "giant", "vampire", "cat", "half-giant", "acromantula",
                 "hippogriff", "poltergeist", "dragon", "ghost", "owl", "goblin", "human", "half-human", "werewolf"]
by_species = {i: list() for i in species_names}

hogwarts_students = list()
hogwarts_staffs = list()


cont = 1
for i in _characters_list:
    all_characters.append(Character(i))
    for j in i:
        if j == 'hogwartsStudent':
            if i[j]:
                hogwarts_students.append(i)
        if j == 'hogwartsStaff':
            if i[j]:
                hogwarts_staffs.append(i)
        if j == 'house':
            if i[j] in hogwarts_houses:
                hogwarts_houses[i[j]].append(i)
        if j == 'ancestry':
            if i[j] in ancestry_names:
                by_ancestries[i[j]].append([i['name'], i['id']])
        if j == 'species':
            if i[j] in species_names:
                by_species[i[j]].append([i['name'], i['id']])

