from tkinter import *

from api_config.configuration import movies_colors, functions_list
from api_config.data_api import all_spells, all_characters, hogwarts_students, hogwarts_staffs, hogwarts_houses
from app.actions import processing_search, processing_select, processing_play, processing_item


class AppMain:

    def __init__(self):

        self.selected = None
        standard_size = 2

        self.window = Tk()
        self.window.title('HP - API')
        self.window.geometry("+300+200")
        self.window.resizable(False, False)
        self.window.config(bg=movies_colors['black'], bd=3)

        color_frames = movies_colors['black'], movies_colors['brown']
        color_sub_frames = [movies_colors['yellow'], movies_colors['black'], movies_colors['beige']]

        self.frame_top = Frame(self.window, bg=color_frames[0], bd=10)

        frame_entry = Frame(self.frame_top)
        color_entry = movies_colors['grey']

        self.entry = Entry(frame_entry, width=(standard_size * 61), disabledbackground=color_entry)
        self.entry.config(bg=color_entry, bd=4, state=DISABLED)
        self.entry.pack()

        frame_entry.pack()

        self.frame_top.pack(side=TOP)

        self.frame_left = Frame(self.window, bg=color_frames[0], bd=10)

        frame_search = Frame(self.frame_left, bg=color_sub_frames[0], bd=1)
        color_search = [movies_colors['grey'], movies_colors['white'], movies_colors['yellow']]

        self.search_list = ["character", "actor", "house", "spell", "species", "ancestry"]

        self.string_menu = StringVar(self.window)
        self.string_menu.set("Improve search")
        improve_search = OptionMenu(frame_search, self.string_menu, *self.search_list, self.string_menu.get())
        improve_search.config(bg=color_search[0], activebackground=color_search[1], highlightbackground=color_search[2])
        improve_search.config(width=(standard_size * 22))
        improve_search.pack()

        self.entry_search = Entry(frame_search, width=(standard_size * 9), bd=4, state=NORMAL, bg=color_search[1])
        self.entry_search.config(highlightbackground=color_search[2], disabledbackground=color_search[0])
        self.entry_search.pack(side=LEFT)

        Button(frame_search, text='search',
               command=self.do_search, width=7, bg=color_search[0]).pack(side=LEFT)
        Label(frame_search, text='API - HP',
              font=('Arial', 10, 'bold'), width=(standard_size * 3), background=color_search[2]).pack(side=BOTTOM)

        frame_search.pack(fill=Y)

        frame_spinbox = Frame(self.frame_left, bg=color_sub_frames[2], bd=7)
        color_spinbox = [movies_colors['grey'], movies_colors['white'], movies_colors['black']]

        self.menu_play_list = ['Characters', 'Hogwarts', 'Curiosities']

        self.spinbox = Spinbox(frame_spinbox, values=self.menu_play_list)
        self.spinbox.config(width=(standard_size * 20), bg=color_spinbox[0], bd=8)
        self.spinbox.config(highlightbackground=color_spinbox[1])
        self.spinbox.pack(side=LEFT)

        self.string_play = StringVar(self.window)
        self.string_play.set('>')
        but_play = Button(frame_spinbox, font=('consolas', 13, 'bold'), textvariable=self.string_play,
                          command=self.to_play)
        but_play.config(width=(standard_size * 1), height=1, bd=2, bg=color_spinbox[0],
                        highlightbackground=color_spinbox[1])
        but_play.pack(side=LEFT)

        frame_spinbox.pack()

        frame_prev_nex = Frame(self.frame_left, bg=color_sub_frames[1], bd=0)

        self.string_previous = StringVar(self.window)
        self.string_previous.set(' [-] ')
        previous = Button(frame_prev_nex, textvariable=self.string_previous, command=self.previous)
        previous.config(width=(standard_size * 10), bd=4, fg=color_spinbox[2])
        previous.pack(side=LEFT)

        self.string_next = StringVar(self.window)
        self.string_next.set(' [-] ')
        go_next = Button(frame_prev_nex, textvariable=self.string_next, command=self.next)
        go_next.config(width=(standard_size * 10), bd=4, fg=color_spinbox[2])
        go_next.pack(side=LEFT)

        frame_prev_nex.pack()

        frame_listbox = Frame(self.frame_left, bg=color_sub_frames[1], bd=1)
        color_listbox = [movies_colors['grey'], movies_colors['white'], movies_colors['black']]

        self.listbox = Listbox(frame_listbox, width=(standard_size * 15), height=20, bd=20)
        self.listbox.config(bg=color_listbox[0], highlightbackground=color_listbox[1])
        y_scroll_list = Scrollbar(frame_listbox, orient=VERTICAL, command=self.listbox.yview)
        y_scroll_list.grid(row=1, column=0, sticky=N + S)
        self.listbox.config(yscrollcommand=y_scroll_list.set)
        self.listbox.grid(row=1, column=1)

        frame_listbox.pack(side=LEFT)

        frame_but = Frame(self.frame_left, bg=color_sub_frames[1], bd=1)

        self.str_select = StringVar(self.window)
        self.str_select.set('     select     ')
        self.str_exe = StringVar(self.window)
        self.str_exe.set('show more')
        cont = 0
        while cont < 14:
            if cont == 1:
                self.but_select = Button(frame_but, textvariable=self.str_select, command=self.do_select,
                                         state=DISABLED)
                self.but_select.grid(row=cont, column=0)
                cont += 1
            elif cont == 2:
                self.but_execute = Button(frame_but, textvariable=self.str_exe, command=self.show_item, state=DISABLED)
                self.but_execute.grid(row=cont, column=0)
                cont += 1
            else:
                Button(frame_but, text=f'{" " * 20}', bg=color_listbox[0], state=DISABLED).grid(row=cont, column=0)
                cont += 1

        frame_but.pack(side=LEFT)

        self.frame_left.pack(side=LEFT)

        self.frame_right = Frame(self.window, bg=color_frames[0], bd=10)

        frame_text = Frame(self.frame_right, bg=color_sub_frames[0])
        color_text = [movies_colors['grey'], movies_colors['white'], movies_colors['black']]

        self.text = Text(frame_text, width=(standard_size * 25), height=32, bd=20, bg=color_text[2], fg=color_text[1])
        y_scroll_txt = Scrollbar(frame_text, orient=VERTICAL, command=self.text.yview)
        y_scroll_txt.grid(row=1, column=1, sticky=N + S)
        self.text.config(yscrollcommand=y_scroll_txt.set)
        self.text.grid(row=1, column=0)

        frame_text.pack()

        self.frame_right.pack(side=RIGHT)

        self.window.mainloop()

    def next(self):

        try:
            index = self.listbox.curselection()[0] + 1
            self.listbox.select_clear(0, END)
            self.listbox.activate(index)
            self.listbox.select_set(index)
            self.listbox.yview(index - 15)
            self.listbox.select_anchor(index)

        except IndexError:
            self.listbox.select_set(0)

    def previous(self):

        try:
            index = self.listbox.curselection()[0] - 1
            self.listbox.select_clear(0, END)
            self.listbox.activate(index)
            self.listbox.select_set(index)
            self.listbox.yview(index - 15)
            self.listbox.select_anchor(index)

        except Exception as ex:
            self.listbox.select_set(END)
            print(f"No previous\n\nError{ex}")

    def to_play(self):
        self.but_select.config(state=NORMAL)
        self.but_execute.config(state=DISABLED)

        captured = self.spinbox.get()
        processed = processing_play(captured)

        self.text.delete(1.0, END)
        self.listbox.delete(0, END)

        for i in processed:
            self.listbox.insert(END, i)

        self.listbox.select_set(0)
        index = self.listbox.curselection()[0]
        self.listbox.select_anchor(index)

        self.string_previous.set('<<<')
        self.string_next.set('>>>')

    def do_select(self):

        self.selected = self.listbox.get(ANCHOR)
        selected = self.selected

        self.listbox.delete(0, END)
        self.text.delete(1.0, END)

        if selected == '':
            self.listbox.insert(END, 'No item')

        else:
            self.but_execute.config(state=NORMAL)
            self.but_select.config(state=DISABLED)

            processed = processing_select(selected)

            for i in processed[0]:
                self.listbox.insert(END, i)

            self.text.insert(1.0, processed[1])
            for i in processed[2]:
                self.text.insert(END, i)

            try:
                self.listbox.select_set(0)
                index = self.listbox.curselection()[0]
                self.listbox.select_anchor(index)
            except IndexError:
                pass

    def show_item(self):

        selected_before = self.selected
        item_to_show = self.listbox.get(ANCHOR)

        self.text.delete(1.0, END)

        processed = processing_item(selected_before, item_to_show)

        self.text.insert(1.0, processed[0])
        for i in processed[1]:
            self.text.insert(END,  f'{i}')

    def do_search(self):
        self.but_execute.config(state=DISABLED)
        self.but_select.config(state=DISABLED)

        word_captured = self.entry_search.get()
        improve = self.string_menu.get()

        improve_research_enabled = None
        if improve in self.search_list:
            improve_research_enabled = True
        elif improve == "Improve search":
            improve_research_enabled = False

        processed = processing_search(improve, improve_research_enabled, word_captured)

        self.listbox.delete(0, END)

        self.listbox.insert(1, '  Search Result  ', '')
        for i in processed[0]:
            self.listbox.insert(END, i)

        self.text.delete(1.0, END)

        self.text.insert(1.0, 'Details\n\n\n')
        for i in processed[1]:
            self.text.insert(END, f'{i}\n')

        self.string_menu.set("Improve search")


AppMain()
