from tkinter import Tk, StringVar
from revolver.ui.autocomplete_entry import AutoCompleteEntry
import unittest
import types

class AutoCompleteEntryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        list_of_names = [str(x) for x in range(60000)]

        tk_root = Tk()
        sv = StringVar()

        def matches(fieldValue, acListEntry):
            pattern = re.compile(re.escape(fieldValue) + '.*')
            return re.match(pattern, acListEntry)

        self.entry = AutoCompleteEntry(list_of_names, tk_root,
                                       matches_function=matches)
        self.entry.grid(row=0, column=0)

        # tk_root.mainloop()

    def tearDown(self):
        pass

    def create(self, **kwargs):
        return AutoCompleteEntry(self.root, **kwargs)

    def test_basic_autocomplete_entry(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_auto_complete_list_initalized(self):
        self.assertEqual(self.entry.autocomplete_list,
                         [str(x) for x in range(60000)])

    def test_custom_matches_function_initalized(self):
        self.assertIsInstance(self.entry.matches_function, types.FunctionType)

    def test_correct_autocomplete_results(self):
        pass

class AutoCompleteEntryPerformanceTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
