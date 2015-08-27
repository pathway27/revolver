from tkinter import Tk, StringVar
from types import MethodType, FunctionType

from revolver.ui.autocomplete_entry import AutoCompleteEntry

import unittest

class AutoCompleteEntryTest(unittest.TestCase):
    def setUp(self):
        list_of_names = [str(x) for x in range(60000)]

        tk_root = Tk()
        sv = StringVar()
        sv.set("hello")

        def matches(fieldValue, acListEntry):
            pattern = re.compile(re.escape(fieldValue) + '.*')
            return re.match(pattern, acListEntry)

        self.entry_default_args = AutoCompleteEntry(list_of_names, tk_root)

        self.entry_custom_args = AutoCompleteEntry(list_of_names, tk_root,
                                                   list_box_length=12,
                                                   matches_function=matches,
                                                   textvariable=sv)

    def tearDown(self):
        pass

    def create(self, **kwargs):
        return AutoCompleteEntry(self.root, **kwargs)

    def test_auto_complete_list_initalized(self):
        self.assertEqual(self.entry_default_args.autocomplete_list,
                         [str(x) for x in range(60000)])
        self.assertEqual(self.entry_custom_args.autocomplete_list,
                         [str(x) for x in range(60000)])

    def test_default_list_box_length_initalized(self):
        self.assertEqual(self.entry_default_args.list_box_length, 8)

    def test_default_matches_function_initalized(self):
        self.assertIsInstance(self.entry_default_args.matches_function,
                              MethodType)

    def test_default_textvariable_initalized(self):
        self.assertEqual(self.entry_default_args.textvariable.get(), '')

    def test_default_matches_function_results(self):
        self.entry_default_args._default_match('hi', 'hi')

    def test_custom_list_box_length_initalized(self):
        self.assertEqual(self.entry_custom_args.list_box_length, 12)

    def test_custom_matches_function_initalized(self):
        self.assertIsInstance(self.entry_custom_args.matches_function,
                              FunctionType)

    def test_custom_textvariable_initalized(self):
        self.assertEqual(self.entry_custom_args.textvariable.get(), 'hello')

    def test_basic_change_event(self):
        pass

    def test_basic_autocomplete_entry(self):
        self.assertEqual('foo'.upper(), 'FOO')

class AutoCompleteEntryPerformanceTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
