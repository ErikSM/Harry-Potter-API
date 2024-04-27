from tkinter import *

from api_config.configuration import movies_colors, functions_list
from api_config.data_api import houses_names, all_ancestry_type, all_species, all_spells, all_characters, \
    hogwarts_students, hogwarts_staffs, hogwarts_houses


class AppMain:

    def __init__(self):

        self.selected = None

        self.window = Tk()
        self.window.title('HP - API')
        self.window.geometry("+300+200")
        self.window.resizable(False, False)
        self.window.config(bg=movies_colors['black'], bd=3)

        color_frames = movies_colors['black']

        self.frame_top = Frame(self.window, bg=color_frames, bd=10)

        color_entry = movies_colors['grey']

        frame_entry = Frame(self.window)
        self.entry = Entry(frame_entry, width=82, disabledbackground=color_entry)
        self.entry.config(bg=color_entry, bd=4, state=DISABLED)
        self.entry.pack()
        frame_entry.pack()

        self.frame_top.pack(side=TOP)

        self.frame_left = Frame(self.window, bg=color_frames, bd=10)

        color_sub_frames = [movies_colors['yellow'], movies_colors['black'], movies_colors['beige']]

        frame_search = Frame(self.frame_left, bg=color_sub_frames[0], bd=1)
        colors_title = (movies_colors['grey'], movies_colors['white'], movies_colors['yellow'])

        self.menu_improve_list = ["character", "actor", "house", "spell", "species", "ancestry"]

        self.option_menu_name = StringVar(self.window)
        self.option_menu_name.set("Improve search")
        improve_menu = OptionMenu(frame_search, self.option_menu_name, *self.menu_improve_list,
                                  self.option_menu_name.get())
        improve_menu.config(width=32, bg=colors_title[0], activebackground=colors_title[1])
        improve_menu.config(highlightbackground=colors_title[2])
        improve_menu.pack()

        self.field_search = Entry(frame_search, width=10, disabledbackground=colors_title[0], bd=4, state=NORMAL)
        self.field_search.config(bg=colors_title[1], highlightbackground=colors_title[2])
        self.field_search.pack(side=LEFT)

        Button(frame_search, text='search', command=self.do_search, bg=colors_title[0]).pack(side=LEFT)
        Label(frame_search, text='API - HP', font=('Arial', 10, 'bold'), width=13, background=colors_title[2]).pack(
            side=LEFT)
        frame_search.pack(fill=Y)

        boxes_left_colors = [movies_colors['grey'], movies_colors['white'], movies_colors['black']]

        self.menu_play_list = ['Characters', 'Hogwarts', 'Spells', 'Curiosities']

        frame_spinbox = Frame(self.frame_left, bg=color_sub_frames[2], bd=7)
        self.spinbox = Spinbox(frame_spinbox, values=self.menu_play_list)
        self.spinbox.config(width=29, bg=boxes_left_colors[0], bd=7)
        self.spinbox.config(highlightbackground=boxes_left_colors[1])
        self.spinbox.pack(side=LEFT)

        self.string_play = StringVar(self.window)
        self.string_play.set('>')
        play = Button(frame_spinbox, font=('consolas', 13, 'bold'), textvariable=self.string_play, command=self.play)
        play.config(width=2, height=1, bd=1, bg=boxes_left_colors[0], highlightbackground=boxes_left_colors[1])
        play.pack(side=LEFT)
        frame_spinbox.pack()

        frame_prev_nex = Frame(self.frame_left, bg=color_sub_frames[1], bd=0)
        self.string_previous = StringVar(self.window)
        self.string_previous.set(' [-] ')
        self.string_select = StringVar(self.window)
        self.string_select.set(' | [select] > ')
        self.string_next = StringVar(self.window)
        self.string_next.set(' [-] ')

        standard_size = 10

        previous = Button(frame_prev_nex, textvariable=self.string_previous, command=self.previous)
        previous.config(width=(standard_size - 4), bd=2, fg=boxes_left_colors[2])
        previous.pack(side=LEFT)
        select = Button(frame_prev_nex, textvariable=self.string_select, command=self.select)
        select.config(width=(standard_size + 8), bd=3, fg=boxes_left_colors[2])
        select.pack(side=LEFT)
        go_next = Button(frame_prev_nex, textvariable=self.string_next, command=self.next)
        go_next.config(width=(standard_size - 4), bd=2, fg=boxes_left_colors[2])
        go_next.pack(side=LEFT)
        frame_prev_nex.pack()

        frame_list = Frame(self.frame_left, bg=color_sub_frames[1], bd=1)
        self.listbox = Listbox(frame_list, width=30, height=20, highlightbackground=boxes_left_colors[1])
        self.listbox.config(bg=boxes_left_colors[0], bd=20)
        y_text_right = Scrollbar(frame_list, orient=VERTICAL, command=self.listbox.yview)
        y_text_right.grid(row=1, column=0, sticky=N + S)
        self.listbox.grid(row=1, column=1)
        self.listbox.config(yscrollcommand=y_text_right.set)
        frame_list.pack(side=LEFT)

        frame_but = Frame(self.frame_left, bg=color_sub_frames[1], bd=1)
        cont = 0
        while cont < 14:
            if cont == 1:
                self.but_execute = Button(frame_but, text='show more', command=self.show_item, state=DISABLED)
                self.but_execute.grid(row=cont, column=0)
                cont += 1
            else:
                Button(frame_but, text=f'{" "*20}', bg=boxes_left_colors[0], state=DISABLED).grid(row=cont, column=0)
                cont += 1
        frame_but.pack(side=LEFT)

        self.frame_left.pack(side=LEFT)

        self.frame_right = Frame(self.window, bg=color_frames, bd=10)

        frame_text = Frame(self.frame_right)
        self.text = Text(frame_text, width=40, height=30, bg=boxes_left_colors[2], fg=boxes_left_colors[1], bd=20)
        y_text_right = Scrollbar(frame_text, orient=VERTICAL, command=self.text.yview)
        y_text_right.grid(row=1, column=1, sticky=N + S)
        self.text.grid(row=1, column=0)
        frame_text.pack()

        self.frame_right.pack(side=RIGHT)

        self.window.mainloop()

    def show_item(self):

        item = self.listbox.get(ANCHOR)
        self.text.delete(1.0, END)

        for i in functions_list:
            if i[0] == self.selected:
                continue
            else:
                pass

        if self.selected == 'Characters':
            for i in all_characters:
                if item == i.name:
                    self.text.insert(END, f'*({item})\n\n\n')

                    info = i.all_info()
                    for j in info:
                        self.text.insert(END, f'{j}\n')

    #  ------------   in progress   -----------------

    def select(self):

        self.selected = self.listbox.get(ANCHOR)
        selected = self.selected

        self.listbox.delete(0, END)
        self.text.delete(1.0, END)

        hog_students = hogwarts_students
        hog_staffs = hogwarts_staffs
        hog_houses = hogwarts_houses

        if selected == '':
            self.listbox.insert(END, 'No item')

        else:
            self.but_execute.config(state=NORMAL)

        if selected == 'Characters':
            for i in all_characters:
                self.listbox.insert(END, i.name)
                self.text.insert(END, f"({i.code_id}): {i.name}\n\n")
        elif selected == "Specific Character":
            print('not yet')
        elif selected == 'Students':
            for i in hog_students:
                self.listbox.insert(END, i['name'])
                self.text.insert(END, f"{i['name']}: {i['id']}\n\n")
        elif selected == 'Staffs':
            for i in hog_staffs:
                self.listbox.insert(END, i['name'])
                self.text.insert(END, f"{i['name']}: {i['id']}\n\n")
        elif selected == 'Houses':
            for i in hog_houses:
                self.listbox.insert(END, i)
                self.text.insert(END, f"{i}: {len(hog_houses[i])} students\n\n")
        elif selected == 'Spells':
            for i in all_spells:
                self.listbox.insert(END, i['name'])
                self.text.insert(END, f"{i['name']}: {i['description']}\n\n")
        else:
            print('else')

    #  --------------------------------------------------

    def next(self):

        try:
            index = self.listbox.curselection()[0] + 1
            self.listbox.select_clear(0, END)
            self.listbox.activate(index)
            self.listbox.select_set(index)
            self.listbox.yview(index)

        except Exception as ex:
            self.listbox.select_set(0)
            print(f"No next\n\n{ex}")

    def previous(self):

        try:
            index = self.listbox.curselection()[0] - 1
            self.listbox.select_clear(0, END)
            self.listbox.activate(index)
            self.listbox.select_set(index)
            self.listbox.yview(index)
            print(index)

        except Exception as ex:
            self.listbox.select_set(END)
            print(f"No previous\n\nError{ex}")

    def play(self):
        self.listbox.delete(0, END)

        captured = self.spinbox.get()
        options_list = list()

        for i in functions_list:
            value = i[1]
            option = i[0]

            if captured == 'Characters':
                if value == 1:
                    options_list.append(option)
            elif captured == 'Hogwarts':
                if value == 2:
                    options_list.append(option)
            elif captured == 'Spells':
                if value == 3:
                    options_list.append(option)
            elif captured == 'Curiosities':
                if value == 4:
                    options_list.append(option)

        for i in options_list:
            self.listbox.insert(END, i)

        self.listbox.select_set(0)

        self.string_previous.set('<<<')
        self.string_next.set('>>>')

    def do_search(self):
        improve_research_enabled = None

        word_captured = self.field_search.get()
        improve = self.option_menu_name.get()

        if improve in self.menu_improve_list:
            improve_research_enabled = True
        elif improve == "Improve search":
            improve_research_enabled = False

        self.listbox.delete(0, END)

        characters = all_characters
        spells = all_spells
        houses = houses_names
        species = all_species
        ancestries = all_ancestry_type

        character_name = ''
        actor_name = ''
        house_name = ''
        spell_name = ''
        specie_name = ''
        ancestry_type = ''

        type_found = "Not founded"
        to_print = "Not founded"

        founded = False

        a_character = False
        a_actor = False
        a_house = False
        a_spell = False
        a_specie = False
        a_ancestry = False

        if not improve_research_enabled or improve == 'character':
            for i in characters:
                if i.name.title() == word_captured.title():
                    founded = True
                    a_character = True
                    character_name = i.name
                    type_found = "character"
                if i.actor == word_captured:
                    founded = True
                    a_actor = True
                    actor_name = i.actor
                    type_found = "actor"

        if not improve_research_enabled or improve == 'house':
            for i in houses:
                if i.title() == word_captured.title():
                    founded = True
                    a_house = True
                    house_name = i
                    type_found = "house"

        if not improve_research_enabled or improve == 'spell':
            for i in spells:
                for j in i:
                    if j == 'name':
                        if i[j].title() == word_captured.title():
                            founded = True
                            a_spell = True
                            spell_name = i[j]
                            type_found = "spell"

        if not improve_research_enabled or improve == 'specie':
            for i in species:
                if i.title() == word_captured.title():
                    founded = True
                    a_specie = True
                    specie_name = i
                    type_found = 'specie'

        if not improve_research_enabled or improve == 'ancestry':
            for i in ancestries:
                if i.title() == word_captured.title():
                    founded = True
                    a_ancestry = True
                    ancestry_type = i
                    type_found = 'ancestry'

        if founded:
            self.listbox.insert(END, f"was sought:({word_captured})")

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

            self.listbox.insert(END, f"OK founded: {to_print}*")
            self.listbox.insert(END, f"type:[[{type_found}]]")

        else:
            self.listbox.insert(END, to_print)

        self.option_menu_name.set("Improve search")


AppMain()
