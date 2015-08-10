"""
https://gist.github.com/uroshekic/11078820
Inspired by http://code.activestate.com/recipes/578253-an-entry-with-autocompletion-for-the-tkinter-gui/
Changes:
    - Fixed AttributeError: 'AutocompleteEntry' object has no attribute 'listbox'
    - Fixed scrolling listbox
    - Case-insensitive search
    - Added focus to entry field
    - Custom listbox length, listbox width matches entry field width
    - Custom matches function
"""

from tkinter import *
from tkinter.ttk import *
import re

class AutoCompleteEntry(Entry):
    def __init__(self, autocomplete_list, list_box_length=8, *args, **kwargs):
        self.check_kwargs(**kwargs)

        Entry.__init__(self, *args, **kwargs)
        self.focus()
        self.autocomplete_list = autocomplete_list

        self.var = self['textvariable']
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

    def check_kwargs(self, **kwargs):
        if 'matches_function' in kwargs:
            self.matches_function = kwargs['matches_function']
            del kwargs['matches_function']
        else:
            def matches(query, list_entry):
                pattern = re.compile(re.escape(query) + '.*', re.IGNORECASE)
                return re.match(pattern, list_entry)

            self.matchesFunction = matches


if __name__ == '__main__':
    list_of_names = [ str(x) for x in range(60000) ]

    tk_root = Tk()
    sv = StringVar()

    entry = AutoCompleteEntry(list_of_names, tk_root)
    entry.grid(row=0, column=0)

    tk_root.mainloop()
