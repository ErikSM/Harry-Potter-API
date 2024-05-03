from tkinter import *

from api_config.configuration import movies_colors
from app.actions import processing_search, processing_select, processing_play, processing_item


class AppMain:

    def __init__(self):

        self.play_captured = None
        self.option_selected = None
        self.item_caught = None

        start_local = "..//"
        self.current_local = start_local
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

        self.string_local = StringVar(self.window)
        self.string_local.set(start_local)
        self.entry_local = Entry(frame_entry, width=(standard_size * 61), disabledbackground=color_entry)
        self.entry_local.config(bg=color_entry, bd=4, state=DISABLED, textvariable=self.string_local)
        self.entry_local.pack()

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

        except IndexError:
            self.listbox.select_set(END)

    def to_play(self):
        self.but_select.config(state=NORMAL)
        self.but_execute.config(state=DISABLED)

        self.play_captured = self.spinbox.get()
        captured = self.play_captured

        current_local = self.play_captured
        self._update_local(current_local)

        processed = processing_play(captured)
        options_list = processed

        self.text.delete(1.0, END)

        self.listbox.delete(0, END)
        self.listbox.insert(END, *options_list)

        self.listbox.select_set(0)
        index = self.listbox.curselection()[0]
        self.listbox.select_anchor(index)

        self.string_previous.set('<<<')
        self.string_next.set('>>>')

    def do_select(self):

        self.option_selected = self.listbox.get(ANCHOR)
        selected = self.option_selected

        current_local = self.play_captured, self.option_selected
        self._update_local(*current_local)

        if selected == '':
            self.listbox.insert(END, 'No item')

        else:
            self.but_execute.config(state=NORMAL)
            self.but_select.config(state=DISABLED)

            processed = processing_select(selected)
            list_string, text_title, text_string = processed[0], processed[1], processed[2]

            self.listbox.delete(0, END)
            self.listbox.insert(END, *list_string)

            self.text.delete(1.0, END)
            self.text.insert(1.0, text_title)
            for i in text_string:
                self.text.insert(END, i)

            try:
                self.listbox.select_set(0)
                index = self.listbox.curselection()[0]
                self.listbox.select_anchor(index)
            except IndexError:
                pass

    def show_item(self):

        selected_before = self.option_selected
        self.item_caught = self.listbox.get(ANCHOR)
        item_caught = self.item_caught

        current_local = self.play_captured, self.option_selected, self.item_caught
        self._update_local(*current_local)

        processed = processing_item(selected_before, item_caught)
        title, text_list = processed[0], processed[1]

        self.text.delete(1.0, END)

        self.text.insert(1.0, title)
        for i in text_list:
            self.text.insert(END, i)

    def do_search(self):

        self.but_execute.config(state=DISABLED)
        self.but_select.config(state=DISABLED)

        word_captured = self.entry_search.get()
        improve = self.string_menu.get()

        current_local = f'search_for:[{word_captured}]'
        self._update_local(current_local)

        list_title = '  Search Result  ', ''
        details_title = 'Result Details\n\n\n'

        improve_research_enabled = None
        if improve in self.search_list:
            improve_research_enabled = True
        elif improve == "Improve search":
            improve_research_enabled = False

        processed = processing_search(improve, improve_research_enabled, word_captured)
        result_info, details_info = processed[0], processed[1]

        self.listbox.delete(0, END)

        self.listbox.insert(1, *list_title)
        self.listbox.insert(END, *result_info)

        self.text.delete(1.0, END)

        self.text.insert(END, details_title)
        for i in details_info:
            self.text.insert(END, i)

        self.string_menu.set("Improve search")

    def _update_local(self, *args):
        string = '>'

        for i in args:
            string += f"{i}>"

        local = f'{self.current_local}{string}'

        self.string_local.set(local)


AppMain()

