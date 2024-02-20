from tkinter import *
from configuration import movies_colors, hogwarts_houses, all_species


class AppMain:

    def __init__(self):
        self.window = Tk()
        self.window.title('HP - API')
        self.window.geometry("+300+200")
        self.window.resizable(False, False)
        self.window.config(bg=movies_colors['yellow'], bd=3)

        self.entry = Entry(self.window, width=40, disabledbackground=movies_colors['grey'])
        self.entry.config(bg=movies_colors['grey'], bd=1, state=DISABLED)
        self.entry.pack()

        color_frames = movies_colors['dark_pink']

        self.frame_top = Frame(self.window, bg=color_frames, bd=10)
        self.frame_top.pack(side=TOP)
        self.frame_left = Frame(self.window, bg=color_frames, bd=10)
        self.frame_left.pack(side=LEFT)
        self.frame_right = Frame(self.window, bg=color_frames, bd=10)
        self.frame_right.pack(side=RIGHT)
        self.frame_foot = Frame(self.window, bg=color_frames, bd=10)
        self.frame_foot.pack(side=BOTTOM)

        color_sub_frames = movies_colors['yellow']

        self.option_frame_left = Frame(self.frame_left, bg=color_sub_frames, bd=1)
        self.option_frame_left.pack()
        self.list_frame_left = Frame(self.frame_left, bg=color_sub_frames, bd=1)
        self.list_frame_left.pack()
        self.button_frame_left = Frame(self.frame_left, bg=color_sub_frames, bd=1)
        self.button_frame_left.pack()

        self.houses_list = hogwarts_houses
        self.species_list = all_species

        color_option_menu = (movies_colors['grey'], movies_colors['green'], movies_colors['green'])

        self.option_menu_name = StringVar(self.window)
        self.option_menu_name.set("Hogwarts Houses")

        question_menu = OptionMenu(self.option_frame_left, self.option_menu_name,*self.houses_list)
        question_menu.config(width=32, bg=color_option_menu[0], activebackground=color_option_menu[1])
        question_menu.config(highlightbackground=color_option_menu[2])
        question_menu.pack()

        self.option_menu_name_2 = StringVar(self.window)
        self.option_menu_name_2.set("all species")

        question_menu_2 = OptionMenu(self.option_frame_left, self.option_menu_name_2, *self.species_list)
        question_menu_2.config(width=32, bg=color_option_menu[0], activebackground=color_option_menu[1])
        question_menu_2.config(highlightbackground=color_option_menu[2])
        question_menu_2.pack()

        color_listbox = [movies_colors['green'], 'white']
        self.listbox = Listbox(self.list_frame_left, width=30, height=20, highlightbackground=color_listbox[1])
        self.listbox.config(bg=color_listbox[0], bd=20)
        y_list_left = Scrollbar(self.list_frame_left, orient=VERTICAL, command=self.listbox.yview)
        y_list_left.grid(row=1, column=0, sticky=N + S)
        self.listbox.grid(row=1, column=1)
        self.listbox.config(yscrollcommand=y_list_left.set)

        color_buttons = movies_colors['grey']
        self.butom_1 = Button(self.button_frame_left, text="test_house", command=self.print_houses)
        self.butom_1.config(bg=color_buttons, bd=1)
        self.butom_1.pack(side="left")

        self.butom_2 = Button(self.button_frame_left, text='test_species', command=self.print_species)
        self.butom_2.config(bg=color_buttons, bd=1)
        self.butom_2.pack(side="left")

        self.window.mainloop()

    def print_houses(self):
        captured = self.option_menu_name.get()

        self.listbox.delete(0, END)
        self.listbox.insert(END, captured)

    def print_species(self):
        captured = self.option_menu_name_2.get()

        self.listbox.delete(0, END)
        self.listbox.insert(END, captured)


AppMain()
