from revolver.ui.autocomplete_entry import AutoCompleteEntry
import unittest

class AutoCompleteEntryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def create(self, **kwargs):
        return AutoCompleteEntry(self.root, **kwargs)

    def test_basic_autocomplete_entry(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_auto_complete_list_initalized(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_custom_matches_function_initalized(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_correct_autocomplete_results(self):
        pass

class AutoCompleteEntryPerformanceTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
