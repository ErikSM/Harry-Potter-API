from api_config.configuration import characters_dict_keys


class Character:

    def __init__(self, character_dict: dict):

        try:
            self.__data = character_dict

            self.__name = self.__data['name']
            self.__code_id = self.__data['id']
            self.__actor = self.__data['actor']

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
        string = list()

        for i in self.__data:
            string.append(f"{i}: {self.__data[i]}")

        return string

    @property
    def data(self):
        return self.__data

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id

    @property
    def actor(self):
        return self.__actor

