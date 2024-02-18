import tkinter


class TestingOptionMenu:

    def __init__(self):
        window = tkinter.Tk()
        window.title("Testing OptionMenu")
        window.geometry('400x100')

        values_list = ["One", "Two", "Three", "Four", "Five"]

        self.option_menu_name = tkinter.StringVar(window)
        self.option_menu_name.set("Options")
        question_menu = tkinter.OptionMenu(window, self.option_menu_name, *values_list)
        question_menu.pack()

        button = tkinter.Button(window, text='select', command=self.print_option_selected)
        button.pack()

        window.mainloop()

    def print_option_selected(self):
        print("Selected: {}".format(self.option_menu_name.get()))


TestingOptionMenu()
