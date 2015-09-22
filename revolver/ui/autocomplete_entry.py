#!/usr/bin/env python3
"""
Inspired by: https://gist.github.com/uroshekic/11078820

Changes: Re-write
Todo:
    - Logging
"""

from tkinter import Entry, Listbox, StringVar, END
from tkinter.ttk import Entry
import re


class AutoCompleteEntry(Entry): # pylint: disable=too-many-ancestors
    """
    An entry widget with asdf.
    """
    def __init__(self, autocomplete_list, *args, **kwargs):
        self.autocomplete_list = autocomplete_list
        self.list_box_length = kwargs.pop('list_box_length', 8)
        self.matches_function = kwargs.pop('matches_function',
                                           self._default_match)

        # function to initate_string_var_no_textvariable
        self.textvariable = kwargs.get('textvariable', StringVar())
        self.list_box = None
        super().__init__(*args, **kwargs)
        self.config(textvariable=self.textvariable)
        self.focus()

        self.textvariable.trace('w', self._changed)

    @property
    def existing_list_box(self):
        """
        Check if this instance has its' listbox defined/open.
        """
        return self.__dict__.get('list_box', False)

    @staticmethod
    def _default_match(query, list_entry):
        """
        The default match function if none is given during instantiation.
        """
        pattern = re.compile(re.escape(query) + '.*', re.IGNORECASE)
        return re.match(pattern, list_entry)

    def _changed(self, name, index, mode):
        """
        Event handler for changes to entry.
        """
        print("in _changed")
        print(name, index, mode)

        if self.textvariable.get():  # not empty string
            words = self.__comparison()

            if not words:
                return self.__delete_existing_list_box()

            if not self.existing_list_box:
                self.list_box = Listbox(width=self["width"],
                                        height=self.list_box_length)
                # looks hacky
                self.list_box.place(
                    x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                self.list_box.delete(0, END)
                for word in words:
                    self.list_box.insert(END, word)
        else:
            self.__delete_existing_list_box()

    def __delete_existing_list_box(self):
        """
        Deletes open listbox.
        """
        if self.existing_list_box:
            self.list_box.destroy()

    # hmmmm
    def __comparison(self):
        """
        Finds words similar to query. TODO
        """
        if len(self.get()) < 3:
            return []
        ans = [w for w in self.autocomplete_list if
               self.matches_function(self.textvariable.get(), w)]
        print(ans)
        return ans[:5]


if __name__ == '__main__':  # pragma: no cover
    from tkinter import Tk, Button
    from tkinter.ttk import Button

    list_of_names = [str(x) for x in range(60000)]

    tk_root = Tk()
    sv = StringVar()

    def matches(fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)

    entry = AutoCompleteEntry(list_of_names, tk_root,
                              matches_function=matches,
                              textvariable=sv)
    entry.grid(row=0, column=0)

    def callback():
        # print(entry.get())
        print(entry.textvariable.get())

    button = Button(tk_root, text="Button", command=callback)
    button.grid(row=1)

    tk_root.mainloop()
