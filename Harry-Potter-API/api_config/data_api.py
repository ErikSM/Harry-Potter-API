from api_config.access import create_generator, make_request


hogwarts_houses = ["gryffindor", "ravenclaw",  "hufflepuff", "slytherin"]


all_species = ["three-headed dog",
               "centaur",
               "house-elf",
               "giant",
               "vampire",
               "cat",
               "half-giant",
               "acromantula",
               "hippogriff",
               "poltergeist",
               "dragon",
               "ghost",
               "owl",
               "goblin",
               "human",
               "half-human",
               "werewolf"]


all_ancestry_type = ["muggle", "squib", "half-blood", "quarter-veela",
                     "muggleborn", "pure-blood", "half-veela"]


all_characters = create_generator(make_request('all characters'))
all_magic_spells = create_generator(make_request('spells'))

all_hogwarts_students = create_generator(make_request('hogwarts students'))
all_hogwarts_staffs = create_generator(make_request('hogwarts staffs'))

hogwarts_houses_students = dict()
for i in hogwarts_houses:
    hogwarts_houses_students[i] = create_generator(make_request('houses', i))
