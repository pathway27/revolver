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
    def __init__(self, autocomplete_list, *args, **kwargs):

        Entry.__init__(self, *args, **kwargs)
        pass

if __name__ == '__main__':
    """
    list_of_names = []
    tk_root = Tk()
    sv = StringVar()

    entry = AutoCompleteEntry(list_of_names, tk_root)
    entry.grid(row=0, column=0)

    root.mainloop()
    """
