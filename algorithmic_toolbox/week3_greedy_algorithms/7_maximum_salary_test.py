import unittest
from functools import cmp_to_key

def compare(num_1, num_2):
    if num_1 + num_2 < num_2 + num_1:
        return -1
    elif num_1 + num_2 > num_2 + num_1:
        return 1
    else:
        return 0


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=cmp_to_key(compare), reverse=True)

    return ''.join(numbers)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(largest_number_naive([1, 9, 3]), '931')  # add assertion here
        self.assertEqual(largest_number_naive([5, 52, 57, 517, 532, 569, 581]), '58157569553252517')
        self.assertEqual(largest_number_naive([0]), '0')
        self.assertEqual(largest_number_naive([8, 52, 57, 5, 581]), '858157552')
        self.assertEqual(largest_number_naive([3, 30, 31]), '33130')
        self.assertEqual(largest_number_naive([8, 80, 89]), '89880')
        self.assertEqual(largest_number_naive([712, 71, 227]), '71712227')






if __name__ == '__main__':
    unittest.main()
