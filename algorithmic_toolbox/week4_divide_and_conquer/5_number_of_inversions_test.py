import unittest
from collections import deque


def merge_sort(nums, inversions):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = deque(merge_sort(nums[:mid], inversions))
    right = deque(merge_sort(nums[mid:], inversions))
    new = []
    while left and right:
        if left[0] <= right[0]:
            new.append(left.popleft())
        else:
            inversions[0] += len(left)
            new.append((right.popleft()))
    return new + list(left) + list(right)


def inversions_naive(nums):
    inversions = [0]
    merge_sort(nums, inversions)
    return inversions[0]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(merge_sort([2, 3, 9, 2, 2], [0]), [2, 2, 2, 3, 9])  # add assertion here]
        self.assertEqual(merge_sort([2, 1, 9, 2, 2], [0]), [1, 2, 2, 2, 9])
        self.assertEqual(merge_sort([11, 11, 11, 4, 2, 0, 9, 34, 8, 10], [0]), [0, 2, 4, 8, 9, 10, 11, 11, 11, 34])

    def test_inversions(self):
        self.assertEqual(inversions_naive([2, 3, 9, 2, 9]), 2)
        self.assertEqual(inversions_naive([2, 3, 9, 2, 2]), 4)


if __name__ == '__main__':
    unittest.main()