# -*- coding: utf-8 -*-
import unittest
import random
from linked_list import * 

class TestLinkedList(unittest.TestCase):

    def test_empty_linked_list_is_empty(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.is_empty(), True)

    def test_linked_list_is_not_empty(self):
        linked_list = LinkedList()
        linked_list.push('Hi')

        self.assertEqual(linked_list.is_empty(), False)

    def test_linked_list_push(self):
        linked_list = LinkedList()
        linked_list.push(2)
        linked_list.push(3)

        self.assertEqual(str(linked_list), "LinkedList [3, 2]")
        self.assertEqual(linked_list.list_length(), 2)

    def test_linked_list_add(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(3)

        self.assertEqual(linked_list.list_length(), 2)
        self.assertEqual(str(linked_list), "LinkedList [2, 3]")

    def test_linked_list_insert(self):
        linked_list = LinkedList()
        linked_list.insert(2, 0)
        linked_list.insert(3, 1)

        self.assertEqual(linked_list.list_length(), 2)
        self.assertEqual(str(linked_list), "LinkedList [2, 3]")

    def test_linked_list_length(self):
        linked_list = LinkedList()

        for i in range(1, 100):
            item = random.randint(1, 10000)
            linked_list.push(item)

        self.assertEqual(linked_list.list_length(), 99)

    def test_empty_linked_list_length(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.list_length(), 0)

    def test_linked_list_top(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(3)
        linked_list.push(4)

        self.assertEqual(linked_list.top(), 4)

    def test_empty_linked_list_top(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.top(), None)

    def test_linked_list_clear(self):
        linked_list = LinkedList()

        for i in range(1, 100):
            item = random.randint(1, 10000)
            linked_list.push(item)

        linked_list.clear()

        self.assertEqual(linked_list.list_length(), 0)

if __name__ == '__main__':
    unittest.main()