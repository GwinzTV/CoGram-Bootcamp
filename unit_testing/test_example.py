'''
demonstration of how to run a simple unit-test
'''
import unittest
import examples as e

class TestExamples(unittest.TestCase):# inheriting from TestCase class in unittest.
    def test_sum_list_with_one_value(self):
        # Arrange
        num_list = [5]
        # Act
        result = e.sum_list(num_list)
        # Assert
        self.assertEqual(result,5)

    
    def test_sum_list_with_two_value(self):
        # Arrange
        num_list = [5,10]
        # Act
        result = e.sum_list(num_list)
        # Assert
        self.assertEqual(result,15)

    
    def test_get_middle_num_from_list(self):
        # Arrange
        num_list = [1,5,8]
        # Act
        result = e.get_middle_value(num_list)
        # Assert
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()