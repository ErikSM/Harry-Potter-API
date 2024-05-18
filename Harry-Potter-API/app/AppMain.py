from tkinter import *

from api_config.configuration import movies_colors, welcome_string, menu_play_and_code, improve_search_list
from app.actions import processing_search, processing_select, processing_play, processing_item


class AppMain:

    def __init__(self):

        self.__play_captured = None
        self.__option_selected = None
        self.__item_caught = None

        self.__current_local = "../"

        standard_size = 2

        self.__window = Tk()
        self.__window.title('HP - API')
        self.__window.geometry("+300+200")
        self.__window.resizable(False, False)
        self.__window.config(bg=movies_colors['black'], bd=3)

        color_frames = movies_colors['black'], movies_colors['brown']
        color_sub_frames = [movies_colors['yellow'], movies_colors['black'], movies_colors['beige']]

        self.f_top = Frame(self.__window, bg=color_frames[0], bd=10)

        f_entry = Frame(self.f_top)
        color_entry = movies_colors['grey']

        self.string_var_local = StringVar(self.__window)
        self.string_var_local.set(self.__current_local)
        self.entry_local = Entry(f_entry, width=(standard_size * 61), disabledbackground=color_entry)
        self.entry_local.config(bg=color_entry, bd=4, state=DISABLED, textvariable=self.string_var_local)
        self.entry_local.pack()

        f_entry.pack()

        self.f_top.pack(side=TOP)

        self.f_left = Frame(self.__window, bg=color_frames[0], bd=10)

        f_search = Frame(self.f_left, bg=color_sub_frames[0], bd=1)
        color_search = [movies_colors['grey'], movies_colors['white'], movies_colors['yellow']]

        self.searches = improve_search_list

        self.string_improve = StringVar(self.__window)
        self.string_improve.set("Improve search")
        improve_menu = OptionMenu(f_search, self.string_improve, *self.searches, self.string_improve.get())
        improve_menu.config(bg=color_search[0], activebackground=color_search[1], highlightbackground=color_search[2])
        improve_menu.config(width=(standard_size * 22))
        improve_menu.pack()

        self.entry_search = Entry(f_search, width=(standard_size * 9), bd=4, state=NORMAL, bg=color_search[1])
        self.entry_search.config(highlightbackground=color_search[2], disabledbackground=color_search[0])
        self.entry_search.pack(side=LEFT)

        Button(f_search, text='search',
               command=self.do_search, width=7, bg=color_search[0]).pack(side=LEFT)
        Label(f_search, text='API - HP',
              font=('Arial', 10, 'bold', 'underline'), width=(standard_size * 3), background=color_search[2]).pack(
            side=BOTTOM)

        f_search.pack(fill=Y)

        f_spin = Frame(self.f_left, bg=color_sub_frames[2], bd=7)
        color_spinbox = [movies_colors['grey'], movies_colors['white'], movies_colors['black']]

        spinbox_list = [i for i in menu_play_and_code]

        self.spinbox = Spinbox(f_spin, values=spinbox_list)
        self.spinbox.config(width=(standard_size * 20), bg=color_spinbox[0], bd=8)
        self.spinbox.config(highlightbackground=color_spinbox[1])
        self.spinbox.pack(side=LEFT)

        self.string_play = StringVar(self.__window)
        self.string_play.set('>')
        but_play = Button(f_spin, font=('consolas', 13, 'bold'), textvariable=self.string_play,
                          command=self.to_play)
        but_play.config(width=(standard_size * 1), height=1, bd=2, bg=color_spinbox[0],
                        highlightbackground=color_spinbox[1])
        but_play.pack(side=LEFT)

        f_spin.pack()

        f_pre_nex = Frame(self.f_left, bg=color_sub_frames[1], bd=0)

        self.string_previous = StringVar(self.__window)
        self.string_previous.set(' [-] ')
        previous = Button(f_pre_nex, textvariable=self.string_previous, command=self.previous)
        previous.config(width=(standard_size * 10), bd=4, fg=color_spinbox[2])
        previous.pack(side=LEFT)

        self.string_next = StringVar(self.__window)
        self.string_next.set(' [-] ')
        go_next = Button(f_pre_nex, textvariable=self.string_next, command=self.next)
        go_next.config(width=(standard_size * 10), bd=4, fg=color_spinbox[2])
        go_next.pack(side=LEFT)

        f_pre_nex.pack()

        f_list = Frame(self.f_left, bg=color_sub_frames[1], bd=1)
        color_listbox = [movies_colors['grey'], movies_colors['white'], movies_colors['black']]

        self.listbox = Listbox(f_list, width=(standard_size * 15), height=20, bd=20)
        self.listbox.config(bg=color_listbox[0], highlightbackground=color_listbox[1])
        y_scroll_list = Scrollbar(f_list, orient=VERTICAL, command=self.listbox.yview)
        y_scroll_list.grid(row=1, column=0, sticky=N + S)
        self.listbox.config(yscrollcommand=y_scroll_list.set)
        self.listbox.grid(row=1, column=1)

        f_list.pack(side=LEFT)

        f_but = Frame(self.f_left, bg=color_sub_frames[1], bd=1)

        self.str_select = StringVar(self.__window)
        self.str_select.set('     select     ')
        self.str_exe = StringVar(self.__window)
        self.str_exe.set('show more')

        cont = 0
        while cont < 14:
            if cont == 1:
                self.but_select = Button(f_but, textvariable=self.str_select, command=self.do_select,
                                         state=DISABLED)
                self.but_select.grid(row=cont, column=0)
                cont += 1
            elif cont == 2:
                self.but_execute = Button(f_but, textvariable=self.str_exe, command=self.show_item,
                                          state=DISABLED)
                self.but_execute.grid(row=cont, column=0)
                cont += 1
            else:
                Button(f_but, text=f'{" " * 20}', bg=color_listbox[0], state=DISABLED).grid(row=cont, column=0)
                cont += 1

        f_but.pack(side=LEFT)

        self.f_left.pack(side=LEFT)

        self.f_right = Frame(self.__window, bg=color_frames[0], bd=10)

        f_text = Frame(self.f_right, bg=color_sub_frames[0])
        color_text = [movies_colors['grey'], movies_colors['white'], movies_colors['black']]

        self.text = Text(f_text, width=(standard_size * 25), height=32, bd=20, bg=color_text[2], fg=color_text[1])
        self.text.insert(1.0, welcome_string)
        y_scroll_txt = Scrollbar(f_text, orient=VERTICAL, command=self.text.yview)
        y_scroll_txt.grid(row=1, column=1, sticky=N + S)
        self.text.config(yscrollcommand=y_scroll_txt.set)
        self.text.grid(row=1, column=0)

        f_text.pack()

        self.f_right.pack(side=RIGHT)

        self.__window.mainloop()

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

        self.__play_captured = self.spinbox.get()
        menu_play_captured = self.__play_captured

        current_local = self.__play_captured
        self._update_local(current_local)

        processed = processing_play(menu_play_captured)
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

        self.__option_selected = self.listbox.get(ANCHOR)
        selected = self.__option_selected

        current_local = self.__play_captured, self.__option_selected
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

        selected_before = self.__option_selected
        self.__item_caught = self.listbox.get(ANCHOR)
        item_caught = self.__item_caught

        current_local = self.__play_captured, self.__option_selected, self.__item_caught
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
        improve = self.string_improve.get()

        current_local = f'search_for:[{word_captured}]'
        self._update_local(current_local)

        list_title = '  Search Result  ', ''
        details_title = 'Result Details\n\n\n'

        improve_research_enabled = None
        if improve in self.searches:
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
            self.text.insert(END, f'{i}\n')

        self.string_improve.set("Improve search")

    def _update_local(self, *args):
        string = '/>'

        for i in args:
            string += f"{i}/>"

        local = f'{self.__current_local}{string}'
        self.string_var_local.set(local)


AppMain()
