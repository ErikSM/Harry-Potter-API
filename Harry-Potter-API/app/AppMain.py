from tkinter import *
from configuration import movies_colors, hogwarts_houses, all_species
from main import make_request


class AppMain:

    def __init__(self):
        self.window = Tk()
        self.window.title('HP - API')
        self.window.geometry("+300+200")
        self.window.resizable(False, False)
        self.window.config(bg=movies_colors['yellow'], bd=3)

        color_entry = movies_colors['grey']

        self.entry = Entry(self.window, width=42, disabledbackground=color_entry)
        self.entry.config(bg=movies_colors['grey'], bd=4, state=DISABLED)
        self.entry.pack()

        color_frames = movies_colors['dark_pink']
        color_sub_frames = movies_colors['yellow']

        self.frame_top = Frame(self.window, bg=color_frames, bd=10)
        self.frame_top.pack(side=TOP)

        sub_frame_top = Frame(self.frame_top, bg=color_sub_frames)
        sub_frame_top.pack(fill=Y)

        colors_title = (movies_colors['grey'], movies_colors['white'], movies_colors['yellow'])

        self.field_search = Entry(sub_frame_top, width=10, disabledbackground=colors_title[0], bd=4, state=NORMAL)
        self.field_search.config(bg=colors_title[1], highlightbackground=colors_title[2])
        self.field_search.pack(side=LEFT)

        Button(sub_frame_top, text='search', command=self.print_search, bg=colors_title[0]).pack(side=LEFT)
        Label(sub_frame_top, text='API - HP', font=('Arial', 12), width=13, background=colors_title[2]).pack(side=LEFT)

        self.frame_left = Frame(self.window, bg=color_frames, bd=10)
        self.frame_left.pack(side=LEFT)

        frame_option = Frame(self.frame_left, bg=color_sub_frames, bd=1)
        frame_option.pack()
        frame_list = Frame(self.frame_left, bg=color_sub_frames, bd=1)
        frame_list.pack()
        frame_button = Frame(self.frame_left, bg=color_sub_frames, bd=1)
        frame_button.pack()

        self.houses_list = hogwarts_houses
        self.species_list = all_species

        color_option_menu = (movies_colors['grey'], movies_colors['green'], movies_colors['green'])

        self.option_menu_name = StringVar(self.window)
        self.option_menu_name.set("Hogwarts Houses")
        question_menu = OptionMenu(frame_option, self.option_menu_name, *self.houses_list)
        question_menu.config(width=32, bg=color_option_menu[0], activebackground=color_option_menu[1])
        question_menu.config(highlightbackground=color_option_menu[2])
        question_menu.pack()

        self.option_menu_name_2 = StringVar(self.window)
        self.option_menu_name_2.set("all species")
        question_menu_2 = OptionMenu(frame_option, self.option_menu_name_2, *self.species_list)
        question_menu_2.config(width=32, bg=color_option_menu[0], activebackground=color_option_menu[1])
        question_menu_2.config(highlightbackground=color_option_menu[2])
        question_menu_2.pack()

        color_listbox = (movies_colors['green'], 'white')

        self.listbox = Listbox(frame_list, width=30, height=20, highlightbackground=color_listbox[1])
        self.listbox.config(bg=color_listbox[0], bd=20)
        y_list_left = Scrollbar(frame_list, orient=VERTICAL, command=self.listbox.yview)
        y_list_left.grid(row=1, column=0, sticky=N + S)
        self.listbox.grid(row=1, column=1)
        self.listbox.config(yscrollcommand=y_list_left.set)

        color_buttons = movies_colors['grey']

        butom_1 = Button(frame_button, text="test_house", command=self.print_houses)
        butom_1.config(bg=color_buttons, bd=1)
        butom_1.pack(side="left")

        butom_2 = Button(frame_button, text='test_species', command=self.print_species)
        butom_2.config(bg=color_buttons, bd=1)
        butom_2.pack(side="left")

        self.frame_right = Frame(self.window, bg=color_frames, bd=10)
        self.frame_right.pack(side=RIGHT)

        self.frame_foot = Frame(self.window, bg=color_frames, bd=10)
        self.frame_foot.pack(side=BOTTOM)

        self.window.mainloop()

    def print_houses(self):
        captured = self.option_menu_name.get()

        self.listbox.delete(0, END)
        self.listbox.insert(END, captured)

    def print_species(self):
        captured = self.option_menu_name_2.get()

        self.listbox.delete(0, END)
        self.listbox.insert(END, captured)

    def print_search(self):
        captured = self.field_search.get()



        requested = make_request('all characters')

        print(requested)
        for i in requested:
            for j in i:
                if i == 'name':
                    if i[j] == captured:

                        print("founded")
                        self.listbox.insert(1, f"Fonded ({captured}):")
                        self.listbox.insert(1, i[j])
                    else:
                        self.listbox.insert(1, 'not founded')



AppMain()
