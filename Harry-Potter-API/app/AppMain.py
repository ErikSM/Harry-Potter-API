from tkinter import *

from configuration import movies_colors, hogwarts_houses


class AppMain:

    def __init__(self):

        self.window = Tk()
        self.window.title('HP - API')
        self.window.geometry("+300+200")
        self.window.resizable(False, False)
        self.window.config(bg=movies_colors['yellow'], bd=3)

        self.entry = Entry(self.window, width=40)
        self.entry.config(bg=movies_colors['grey'], bd=1)
        self.entry.pack()

        self.frame = Frame(self.window)
        self.frame.config(bg=movies_colors['dark_pink'], bd=10)
        self.frame.pack()

        self.values_list = hogwarts_houses

        self.option_menu_name = StringVar(self.window)
        self.option_menu_name.set("Hogwarts Houses")

        question_menu = OptionMenu(self.frame, self.option_menu_name, *self.values_list)
        question_menu.config(bg=movies_colors['grey'], width=30)
        question_menu.pack()

        self.listbox = Listbox(self.frame, width=30, height=20)
        self.listbox.config(bg=movies_colors['green'], bd=20)
        self.listbox.pack()

        self.window.mainloop()


AppMain()

