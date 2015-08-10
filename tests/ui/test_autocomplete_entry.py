from revolver.ui.autocomplete_entry import AutoCompleteEntry
import unittest

class AutoCompleteEntryTest(unittest.TestCase):

    def create(self, **kwargs):
        return AutoCompleteEntry(self.root, **kwargs)

    def test_blah(self):
        self.assertEqual('foo'.upper(), 'FOO')

class AutoCompleteEntryPerformanceTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
