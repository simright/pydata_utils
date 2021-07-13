import unittest

from pydata_utils import list_utils


class TestListUtils(unittest.TestCase):
    def test_list_get(self):
        mylist = [1, 2, 3]

        self.assertEqual(list_utils.list_get(mylist, 1), 2)
        self.assertEqual(list_utils.list_get(mylist, 3), None)

    def test_list_set(self):
        mylist = [1, 2, 3]

        list_utils.list_set(mylist, 5, 100)
        self.assertEqual(
            mylist,
            [1, 2, 3, None, None, 100]
        )

    def test_list_unique(self):
        mylist = [1, 2, 3, 3, 5]

        self.assertEqual(
            list_utils.list_unique(mylist),
            [1, 2, 3, 5]
        )

    def test_list_rstrip(self):
        test_list_1 = ['abc', 'def', 'gh', 'gh']
        self.assertEqual(
            list_utils.list_rstrip(test_list_1, 'gh'),
            ['abc', 'def']
        )

        test_list_2 = ['gh', 'gh']
        self.assertEqual(
            list_utils.list_rstrip(test_list_2, 'gh'),
            list()
        )

        test_list_3 = ['abcdefgh']
        self.assertEqual(
            list_utils.list_rstrip(test_list_3, 'gh'),
            ['abcdefgh']
        )
