from api_config.configuration import characters_dict_keys


class Character:

    def __init__(self, character_dict: dict):

        try:
            self.__data = character_dict

            self.__name = self.__data['name']
            self.__code_id = self.__data['id']
            self.__actor = self.__data['actor']
            self.__birth = self.__data['dateOfBirth']
            self.__alive = self.__data['alive']

        except Exception as ex:
            self.__data = dict()

            for i in characters_dict_keys:
                if i == 'name':
                    self.__data['name'] = 'Error'
                elif i == 'id':
                    self.__data['id'] = f'type:({ex})'
                else:
                    self.__data[i] = 'xxx'

            self.__name = self.__data['name']
            self.__code_id = self.__data['id']

    def all_info(self):
        string_info = list()

        for i in self.__data:
            string_info.append(f"{i}: {self.__data[i]}")

        return string_info

    def specie_and_ancestry(self):

        specie = None
        ancestry = None

        for i in self.__data:
            if i == 'species':
                specie = self.__data[i]
            elif i == 'ancestry':
                ancestry = self.__data[i]
            else:
                pass

        return specie, ancestry

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id

    @property
    def actor(self):
        return self.__actor

    @property
    def data(self):
        return self.__data

    @property
    def birth(self):
        return self.__birth

    @property
    def alive(self):
        return self.__alive
