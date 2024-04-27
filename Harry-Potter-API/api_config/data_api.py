from api_config.access import create_generator, make_request
from objects.Character import Character

houses_names = ["gryffindor", "ravenclaw", "hufflepuff", "slytherin"]

all_species = ["three-headed dog", "centaur", "house-elf", "giant", "vampire", "cat", "half-giant", "acromantula",
               "hippogriff", "poltergeist", "dragon", "ghost", "owl", "goblin", "human", "half-human", "werewolf"]

all_ancestry_type = ["muggle", "squib", "half-blood", "quarter-veela", "muggleborn", "pure-blood", "half-veela"]

_characters_requested = create_generator(make_request('all characters'))
_characters_list = list(_characters_requested)

all_characters = list()
hogwarts_students = list()
hogwarts_staffs = list()
hogwarts_houses = {"Gryffindor": list(), "Ravenclaw": list(), "Hufflepuff": list(), "Slytherin": list()}
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

_spells_requested = create_generator(make_request('spells'))
all_spells = list(_spells_requested)

for i in hogwarts_houses:
    print(i)
    print(len(hogwarts_houses[i]))

