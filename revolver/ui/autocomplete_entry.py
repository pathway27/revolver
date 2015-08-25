"""
https://gist.github.com/uroshekic/11078820
Inspired by
http://code.activestate.com/recipes/578253-an-entry-with-autocompletion-for-the-tkinter-gui/

Changes:
    - Re-write
"""

from tkinter import *
from tkinter.ttk import *
import re

class AutoCompleteEntry(Entry):
    def __init__(self, autocomplete_list, *args, **kwargs):
        self.list_box_length = kwargs.pop('list_box_length', 8)
        self.matches_function = kwargs.pop('matches_function',
                                           self._default_match)

        self.textvariable = kwargs.pop('textvariable', StringVar())
        self.autocomplete_list = autocomplete_list

        Entry.__init__(self, *args, **kwargs)

        self.focus()

        # bind events

        # trace when variable is written to
        self.textvariable.trace('w', self._changed)

    def _default_match(self, query, list_entry):
        pattern = re.compile(re.escape(query) + '.*', re.IGNORECASE)
        return re.match(pattern, list_entry)

    def _changed(self, name, index, mode):
        pass

if __name__ == '__main__':  # pragma: no cover
    list_of_names = [ str(x) for x in range(60000) ]

    tk_root = Tk()
    sv = StringVar()

    def matches(fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)

    entry = AutoCompleteEntry(list_of_names, tk_root,
                              matches_function=matches)
    entry.grid(row=0, column=0)

    tk_root.mainloop()
