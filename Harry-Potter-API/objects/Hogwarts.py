from api_config.data_api import all_hogwarts_students, all_hogwarts_staffs, hogwarts_houses, hogwarts_houses_students


class Hogwarts:

    def __init__(self):

        self.students = list(all_hogwarts_students)
        self.staffs = list(all_hogwarts_staffs)

        self.house = dict()
        for i in hogwarts_houses_students:
            self.house[i] = {"students": list(hogwarts_houses_students[i])}

    def find_student(self, search):
        result = 'no'
        name = list()

        for i in self.students:
            for j in i:
                if j == 'name':
                    if i[j] == search:
                        result = 'ok'
                        name.append(i[j])
                    elif i[j] != name:
                        pass

        print(result)
        print(name)

    def show_houses(self):
        for i in self.house:
            print(f"{i}:")
            print(self.house[i])


teste = Hogwarts()
teste.find_student('Victoire Weasley')

