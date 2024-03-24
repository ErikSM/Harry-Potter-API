from api_config.access import make_request, create_generator
from api_config.configuration import id_sample, characters_dict_keys


class Character:

    def __init__(self, code_id):

        try:
            requested = make_request("specific character", code_id)[0]

        except Exception as ex:
            self.__data = dict()
            for i in characters_dict_keys:
                if i == 'name':
                    self.__data['name'] = 'Error'
                elif i == 'id':
                    self.__data['id'] = f'{ex}'
                else:
                    self.__data[i] = 'xxx'

        else:
            self.__data = requested

        finally:
            self.__name = self.__data['name']
            self.__code_id = self.__data['id']

    @property
    def data(self):
        return self.__data

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id


teste = Character(id_sample)
print(teste.data)

