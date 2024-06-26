import unittest
from random import randint


def partition3(array, left, right):
    pivot = array[left]
    m1 = left
    m2 = left
    for i in range(left + 1, right + 1):
        if array[i] == pivot:
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
        elif array[i] < pivot:
            m1 += 1
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
            array[m2], array[m1-1] = array[m1-1], array[m2]

    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)
    return array


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(randomized_quick_sort([2, 3, 9, 2, 2], 0, 4), [2, 2, 2, 3, 9])  # add assertion here]
        self.assertEqual(randomized_quick_sort([2, 1, 9, 2, 2], 0, 4), [1, 2, 2, 2, 9])
        self.assertEqual(randomized_quick_sort([11, 11, 11, 4, 2, 0, 9, 34, 8, 10], 0, 9), [0, 2, 4, 8, 9, 10, 11, 11, 11, 34])


if __name__ == '__main__':
    unittest.main()
