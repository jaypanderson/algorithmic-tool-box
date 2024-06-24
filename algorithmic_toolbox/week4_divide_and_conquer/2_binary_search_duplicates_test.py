import unittest


def binary_search(keys, query):
    l = 0
    r = len(keys) - 1
    while l <= r:
        mid = (l + r) // 2
        if keys[mid] == query:
            break
        elif keys[mid] < query:
            l = mid + 1
        else:
            r = mid - 1
    if l > r:
        return -1

    while l <= r:
        mid = (l + r) // 2
        if mid == len(keys) - 1 or mid == 0:
            return mid
        if keys[mid] != query and keys[mid+1] == query:
            return mid+1
        elif keys[mid] != query:
            l = mid + 1
        elif keys[mid] == query and keys[mid-1] != query:
            return mid
        else:
            r = mid - 1
    return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(binary_search([2, 2, 4, 4, 8], 2), 0)  # add assertion here
        self.assertEqual(binary_search([2, 2, 4, 4, 8], 4), 2)  # add assertion here
        self.assertEqual(binary_search([2, 2, 4, 4, 8], 8), 4)
        self.assertEqual(binary_search([2, 2, 4, 4, 8, 8], 8), 4)
        self.assertEqual(binary_search([2, 2, 4, 4, 8], 1), -1)
        self.assertEqual(binary_search([2, 2, 4, 4, 8], 0), -1)

    def test_1(self):
        self.assertEqual(binary_search([2, 4, 4, 4, 7, 7, 9], 9), 6)
        self.assertEqual(binary_search([2, 4, 4, 4, 7, 7, 9], 4), 1)
        self.assertEqual(binary_search([2, 4, 4, 4, 7, 7, 9], 5), -1)
        self.assertEqual(binary_search([2, 4, 4, 4, 7, 7, 9], 2), 0)




if __name__ == '__main__':
    unittest.main()
