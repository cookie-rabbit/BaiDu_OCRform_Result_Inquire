import unittest

from data_find import DataFind

data_find = DataFind


class ValidSearch(unittest.TestCase):
    """ test data_find.py DataFind.valid_search() """

    def test_word_None(self):
        """ test if word is None or '' """
        target = [{'word': '', 'direct': 4, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_direct_None(self):
        """test if direct is None or '' """
        target = [{'word': 1, 'direct': '', 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_direct_str(self):
        """test if direct is str """
        target = [{'word': 1, 'direct': '3', 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_direct_out_of_list(self):
        """test if direct is out of list(1,2,3,4) """
        target = [{'word': 1, 'direct': 33, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_distance_None(self):
        """test if distance is None """
        target = [{'word': 1, 'direct': 1, 'distance': None, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(TypeError, data_find.valid_search, target)

    def test_distance_lt_0(self):
        """test if distance is little than 0 """
        target = [{'word': 1, 'direct': 1, 'distance': -1, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_distance_str_can_not_int(self):
        """test if distance is str which can't int() """
        target = [{'word': 1, 'direct': 1, 'distance': 'aaa', 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_distance_str_can_int(self):
        """test if distance is str which can int() """
        target_str = [{'word': 1, 'direct': 1, 'distance': '2', 'num': 1, 'format': r'',
                       'accuracy': ('like', 1), 'f_type': 1}, ]

        target_int = [{'word': 1, 'direct': 1, 'distance': 2, 'num': 1, 'format': r'',
                       'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertEqual(data_find.valid_search(target_str), data_find.valid_search(target_int))

    def test_num_None(self):
        """test if distance is None """
        target = [{'word': 1, 'direct': 1, 'distance': 1, 'num': None, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(TypeError, data_find.valid_search, target)

    def test_num_lt_1(self):
        """test if distance is little than 1 """
        target = [{'word': 1, 'direct': 1, 'distance': 1, 'num': 0, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_num_str_can_not_int(self):
        """test if distance is str which can't int() """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 'aaa', 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_num_str_can_int(self):
        """test if distance is str which can int() """
        target_str = [{'word': 1, 'direct': 1, 'distance': 0, 'num': '3', 'format': r'',
                       'accuracy': ('like', 1), 'f_type': 1}, ]

        target_int = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 3, 'format': r'',
                       'accuracy': ('like', 1), 'f_type': 1}, ]
        self.assertEqual(data_find.valid_search(target_str), data_find.valid_search(target_int))

    def test_f_type_None(self):
        """test if f_type is None """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': None}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_f_type_out_of_list(self):
        """test if f_type is out of list(0,1) """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1), 'f_type': 2}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_accuracy_is_not_tuple(self):
        """test if accuracy is not tuple """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ['like', 1], 'f_type': 0}, ]
        self.assertRaises(TypeError, data_find.valid_search, target)

    def test_accuracy_length_gt_2(self):
        """test if accuracy's length is greater than 2 """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', 1, 2), 'f_type': 0}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_accuracy_length_lt_2(self):
        """test if accuracy's length is little than 2 """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like',), 'f_type': 0}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_accuracy_index_0_out_of_list(self):
        """test if accuracy index 0 out of list """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('abc', 1), 'f_type': 0}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_accuracy_index_1_can_not_int(self):
        """test if accuracy index 1 can not int """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', 'a'), 'f_type': 0}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)

    def test_accuracy_index_1_int_lt_0(self):
        """test if accuracy index 1 int little than 0 """
        target = [{'word': 1, 'direct': 1, 'distance': 0, 'num': 1, 'format': r'',
                   'accuracy': ('like', '-1'), 'f_type': 0}, ]
        self.assertRaises(ValueError, data_find.valid_search, target)


if __name__ == '__main__':
    unittest.main(verbosity=2)
