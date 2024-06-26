import unittest
from random import randint


def partition3(array, left, right):
    pivot = array[left]
    m1 = left
    m2 = left
    over = False
    for i in range(left + 1, right + 1):
        if array[i] == pivot:
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
        elif array[i] < pivot:
            m1 += 1
            m2 += 1
            if over:
                array[m2], array[i] = array[i], array[m2]
                array[m1 - 1], array[m2] = array[m2], array[m1 - 1]
            else:
                array[m1 - 1], array[i] = array[i], array[m1 - 1]
        else:
            over = True
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












    #     if array[i] == array[rand]:
    #         rand += 1
    #         m1 += 1
    #         m2 += 1
    #         array[m1], array[i] = array[i], array[m1]
    #         array[rand], array[m1] = array[m1], array[rand]
    #     elif array[i] < array[rand]:
    #         m1 += 1
    #         m2 += 1
    #         array[m1], array[i] = array[i], array[m1]
    #     else:
    #         m2 += 1
    # print(array[left:right+1], rand, m1, m2)
    #
    # count = m1 - rand
    # diff = rand + 1
    # if array[rand] < array[rand + 1]:
    #     print('1: ', array[left:right + 1], left, rand)
    #     return left, rand

    # elif array[rand] > array[m2]:
    #     for i in range(left, left + count + 1):
    #         array[i], array[i + diff] = array[i + diff], array[i]
    #     print('2: ', array[left:right + 1])
    #     return m1 - count + 1, m1

    # for i in range(left, left+count):
    #     array[i], array[i + diff] = array[i + diff], array[i]
    #
    # print('3: ', array[left:right + 1], m1 - count + 1, m1)
    # return m1 - diff + 1, m1





# def partition3(array, left, right):
#     pivot = array[left]
#     m1 = left
#     m2 = left
#     for i in range(left + 1, right + 1):
#         if array[i] == pivot:
#             m2 += 1
#             array[m2], array[i] = array[i], array[m2]
#         elif array[i] < pivot:
#             m1 += 1
#             m2 += 1
#             array[m1], array[i] = array[i], array[m1]
#             if m1 != m2:
#                 array[m2], array[i] = array[i], array[m2]
#     array[left], array[m1] = array[m1], array[left]
#     return m1, m2
#
#
# def randomized_quick_sort(array, left, right):
#     if left >= right:
#         return
#     k = randint(left, right)
#     array[left], array[k] = array[k], array[left]
#     m1, m2 = partition3(array, left, right)
#     randomized_quick_sort(array, left, m1 - 1)
#     randomized_quick_sort(array, m2 + 1, right)
#     return array



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(randomized_quick_sort([2, 3, 9, 2, 2], 0, 4), [2, 2, 2, 3, 9])  # add assertion here]
        self.assertEqual(randomized_quick_sort([2, 1, 9, 2, 2], 0, 4), [1, 2, 2, 2, 9])
        self.assertEqual(randomized_quick_sort([11, 11, 11, 4, 2, 0, 9, 34, 8, 10], 0, 9), [0, 2, 4, 8, 9, 10, 11, 11, 11, 34])


if __name__ == '__main__':
    unittest.main()
