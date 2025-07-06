import unittest
from my_def import *

class TestHomeworks(unittest.TestCase):

    def test_multiplication_table(self):
        self.assertEqual(
            multiplication_table(3),
            ['3x1=3', '3x2=6', '3x3=9', '3x4=12', '3x5=15', '3x6=18', '3x7=21', '3x8=24']
        )

    def test_add_number(self):
        self.assertEqual(add_number(10, 5), 15)

    def test_arithmetic(self):
        self.assertEqual(arithmetic([4, 5, 4, 10]), 5.75)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("some text"), "txet emos")

    def test_len_count(self):
        self.assertEqual(
            len_count(("first", "second", "third", "longest in the list")),
            "longest in the list"
        )

    def test_find_substring_found(self):
        self.assertEqual(find_substring("hello world", "world"), 6)

    def test_find_substring_not_found(self):
        self.assertEqual(find_substring("hello world", "cat"), -1)

    def test_unic_chars_true(self):
        self.assertTrue(unic_chars("abcdefghijklm"))

    def test_unic_chars_false(self):
        self.assertFalse(unic_chars("aaaaaa"))

    def test_character_counter(self):
        self.assertEqual(character_counter("aAaAaA", "a"), 6)

    def test_find_items_by_type_str(self):
        lst = ['1', '2', 3, True, 5.5]
        self.assertEqual(find_items_by_type(lst, 'str'), ['1', '2'])

    def test_employee_list_editor(self):
        lst = [('John', 'Doe', 28, 'Engineer', 'NY')]
        result = employee_list_editor(lst.copy(), 'alice', 'cooper', 30, 'designer', 'la')
        self.assertEqual(result[0], ('Alice', 'Cooper', 30, 'Designer', 'La'))

