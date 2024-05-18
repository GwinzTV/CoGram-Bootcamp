import unittest

from largest_number import largest
from sum_recursion import sum_array
from linklist import SinglyLinkedList


class TestLargestMethods(unittest.TestCase):

    def test_negative_case_largest_number(self):
        # Arrange
        array = ['1', '6', '12', '7', '18', '9', '2']
        # Act
        result = largest(array)
        # Assert
        self.assertEqual(result, 18)

    def test_largest_number(self):
        # Arrrange
        array = [1, 6, 12, 7, 18, 9, 2]
        # Act
        result = largest(array)
        # Assert
        self.assertEqual(result, 18)


class TestSumtMethods(unittest.TestCase):

    def test_sum_array(self):
        # Arrange
        array = [1, 6, 12, 7, 18, 9, 2]
        # Act
        result = sum_array(array, 2)
        # Assert
        self.assertEqual(result, 19)

    def test_negative_case_sum_array(self):
        # Arrange
        array = [1, '6', 12, '7', 18, '9', 2]
        # Act
        result = sum_array(array, 2)
        # Assert
        self.assertEqual(result, 19)


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        # ArrangeAll (to avoid clunky repeats)
        self.sll = SinglyLinkedList()
        for i in range(5):
            self.sll.append(i)

    def test_prepend_data_to_list(self):
        '''
        test for prepend method
        '''
        # arrange
        ll = self.sll
        ll.prepend('99')
        # act
        result = ll.head.data
        # assert
        self.assertEqual(result, '99')

    def test_append_method(self):
        '''
        test for append method
        '''
        # Arrange
        ll = self.sll
        # Act
        ll.append(99)
        last = ll.head
        while last.next is not None:
            last = last.next
        result = last.data
        # Assert
        self.assertEqual(result, 99)

    def test_delete_method(self):
        '''
        test for delete method
        '''
        # Arrange
        ll = self.sll
        # Act
        result = ll.delete(3)
        # Assert
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
