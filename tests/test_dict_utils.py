import unittest

from pydata_utils import dict_utils


class TestDictUtils(unittest.TestCase):
    def test_dict_get_item(self):
        mydict = {
            'key1': {
                'key1.1': 2
            }
        }

        self.assertEqual(dict_utils.dict_get(mydict, ['key1', 'key1.1']), 2)
        self.assertEqual(dict_utils.dict_get(mydict, ['key1', 'badkey']), None)

    def test_dict_set_item(self):
        mydict = {
            'key1': {
                'key1.1': 2
            }
        }

        list_keys = ['key1', 'key1.1']
        dict_utils.dict_set(mydict, list_keys, 3)
        self.assertEqual(dict_utils.dict_get(mydict, list_keys), 3)

        list_keys = ['key1', 'key1.2']
        dict_utils.dict_set(mydict, list_keys, 100)
        self.assertEqual(dict_utils.dict_get(mydict, list_keys), 100)

        list_keys = ['key1', 'key1.3', 'key1.3.1']
        dict_utils.dict_set(mydict, list_keys, 200)
        self.assertEqual(dict_utils.dict_get(mydict, list_keys), 200)

    def test_dict_has_keys(self):
        mydict = {
            'key1': {
                'key1.1': 2
            }
        }

        self.assertTrue(dict_utils.dict_has_keys(mydict, ['key1']))
        self.assertTrue(dict_utils.dict_has_keys(mydict, ['key1', 'key1.1']))

        self.assertFalse(dict_utils.dict_has_keys(mydict, ['key1a', 'key1.1']))
        self.assertFalse(dict_utils.dict_has_keys(mydict, ['key1', 'key1.1', 'key1.1.1']))
