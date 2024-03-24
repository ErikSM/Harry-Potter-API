from tkinter import *

from api_config.access import make_request, create_generator
from api_config.configuration import movies_colors, functions_list
from api_config.data_api import hogwarts_houses, all_ancestry_type, all_species


class AppMain:

    def __init__(self):
        self.window = Tk()
        self.window.title('HP - API')
        self.window.geometry("+300+200")
        self.window.resizable(False, False)
        self.window.config(bg=movies_colors['pink'], bd=3)

        color_entry = movies_colors['grey']

        self.entry = Entry(self.window, width=42, disabledbackground=color_entry)
        self.entry.config(bg=color_entry, bd=4, state=DISABLED)
        self.entry.pack()

        color_frames = "black"
        color_sub_frames = [movies_colors['yellow'], movies_colors['pink'], movies_colors['beige']]

        self.frame_top = Frame(self.window, bg=color_frames, bd=10)
        self.frame_top.pack(side=TOP)

        sub_frame_top = Frame(self.frame_top, bg=color_sub_frames[0], bd=1)
        sub_frame_top.pack(fill=Y)

        colors_title = (movies_colors['grey'], movies_colors['white'], movies_colors['yellow'])

        self.menu_improve_list = ["character", "actor", "house", "spell", "species", "ancestry"]

        self.option_menu_name = StringVar(self.window)
        self.option_menu_name.set("Improve search")
        improve_menu = OptionMenu(sub_frame_top, self.option_menu_name, *self.menu_improve_list)
        improve_menu.config(width=32, bg=colors_title[0], activebackground=colors_title[1])
        improve_menu.config(highlightbackground=colors_title[2])
        improve_menu.pack()

        self.field_search = Entry(sub_frame_top, width=10, disabledbackground=colors_title[0], bd=4, state=NORMAL)
        self.field_search.config(bg=colors_title[1], highlightbackground=colors_title[2])
        self.field_search.pack(side=LEFT)

        Button(sub_frame_top, text='search', command=self.do_search, bg=colors_title[0]).pack(side=LEFT)
        Label(sub_frame_top, text='API - HP', font=('Arial', 12), width=13, background=colors_title[2]).pack(side=LEFT)

        self.frame_left = Frame(self.window, bg=color_frames, bd=10)
        self.frame_left.pack(side=LEFT)

        frame_spinbox = Frame(self.frame_left, bg=color_sub_frames[2], bd=7)
        frame_spinbox.pack()
        frame_prev_nex = Frame(self.frame_left, bg=color_sub_frames[1], bd=0)
        frame_prev_nex.pack()
        frame_list = Frame(self.frame_left, bg=color_sub_frames[1], bd=1)
        frame_list.pack()
        frame_button = Frame(self.frame_left, bg=color_sub_frames[1], bd=1)
        frame_button.pack()

        boxes_left_colors = [movies_colors['grey'], movies_colors['white'], movies_colors['pink']]

        self.menu_hogwarts_list = ['Characters', 'Hogwarts', 'Spells', 'Curiosities']

        self.spinbox = Spinbox(frame_spinbox, values=self.menu_hogwarts_list)
        self.spinbox.config(width=29, bg=boxes_left_colors[0], bd=7)
        self.spinbox.config(highlightbackground=boxes_left_colors[1])
        self.spinbox.pack(side=LEFT)

        self.string_play = StringVar(self.window)
        self.string_play.set('>')

        play = Button(frame_spinbox, font=('consolas', 13, 'bold'), textvariable=self.string_play, command=self.play)
        play.config(width=2, height=1, bd=1, bg=boxes_left_colors[0], highlightbackground=boxes_left_colors[1])
        play.pack(side=LEFT)

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

        self.listbox = Listbox(frame_list, width=30, height=20, highlightbackground=boxes_left_colors[1])
        self.listbox.config(bg=boxes_left_colors[0], bd=20)
        y_list_left = Scrollbar(frame_list, orient=VERTICAL, command=self.listbox.yview)
        y_list_left.grid(row=1, column=0, sticky=N + S)
        self.listbox.grid(row=1, column=1)
        self.listbox.config(yscrollcommand=y_list_left.set)

        color_buttons = movies_colors['grey']

        button_1 = Button(frame_button, text="test_house")
        button_1.config(bg=color_buttons, bd=1)
        button_1.pack(side="left")

        self.frame_right = Frame(self.window, bg=color_frames, bd=10)
        self.frame_right.pack(side=RIGHT)

        self.frame_foot = Frame(self.window, bg=color_frames, bd=10)
        self.frame_foot.pack(side=BOTTOM)

        self.window.mainloop()

    def select(self):
        pass

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

        captured = self.field_search.get()
        improve = self.option_menu_name.get()

        if improve in self.menu_improve_list:
            improve_research_enabled = True
        elif improve == "Improve search":
            improve_research_enabled = False

        self.listbox.delete(0, END)

        characters = create_generator(make_request('all characters'))
        all_spells = create_generator(make_request('spells'))
        all_houses = hogwarts_houses
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
                for j in i:
                    if j == 'name':
                        if i[j] == captured:
                            founded = True
                            a_character = True
                            character_name = i[j]
                            type_found = "character"
                    elif j == 'actor':
                        if i[j] == captured:
                            founded = True
                            a_actor = True
                            actor_name = i[j]
                            type_found = "actor"

        if not improve_research_enabled or improve == 'house':
            for i in all_houses:
                if i == captured:
                    founded = True
                    a_house = True
                    house_name = i
                    type_found = "house"

        if not improve_research_enabled or improve == 'spell':
            for i in all_spells:
                for j in i:
                    if j == 'name':
                        if i[j] == captured:
                            founded = True
                            a_spell = True
                            spell_name = i[j]
                            type_found = "spell"

        if not improve_research_enabled or improve == 'specie':
            for i in species:
                if i == captured:
                    founded = True
                    a_specie = True
                    specie_name = i
                    type_found = 'specie'

        if not improve_research_enabled or improve == 'ancestry':
            for i in ancestries:
                if i == captured:
                    founded = True
                    a_ancestry = True
                    ancestry_type = i
                    type_found = 'ancestry'

        if founded:
            self.listbox.insert(END, f"was sought:({captured})")

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
