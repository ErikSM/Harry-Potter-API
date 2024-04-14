from api_config.access import create_generator, make_request
from objects.Character import Character

hogwarts_houses = ["gryffindor", "ravenclaw", "hufflepuff", "slytherin"]

all_species = ["three-headed dog", "centaur", "house-elf", "giant", "vampire", "cat", "half-giant", "acromantula",
               "hippogriff", "poltergeist", "dragon", "ghost", "owl", "goblin", "human", "half-human", "werewolf"]

all_ancestry_type = ["muggle", "squib", "half-blood", "quarter-veela", "muggleborn", "pure-blood", "half-veela"]


def hogwarts_details():
    all_hogwarts_students = create_generator(make_request('hogwarts students'))
    all_hogwarts_staffs = create_generator(make_request('hogwarts staffs'))

    houses_students = dict()
    for i in hogwarts_houses:
        houses_students[i] = create_generator(make_request('houses', i))

    return all_hogwarts_students, all_hogwarts_staffs, houses_students


_characters_requested = create_generator(make_request('all characters'))
_characters_list = list(_characters_requested)
all_characters = list()
for i in _characters_list:
    all_characters.append(Character(i))

_spells_requested = create_generator(make_request('spells'))
all_spells = list(_spells_requested)

