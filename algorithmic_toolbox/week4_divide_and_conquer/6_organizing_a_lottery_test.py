import unittest
from collections import Counter

# def recur(lines, point, count, i):
#
#
# def points_cover_naive(starts, ends, points):
#     check = set()
#     lines = [[start, end] for start, end in zip(starts, ends)]
#     lines.sort()
#
#
#     count = [0] * len(points)
#     for i, point in enumerate(points):
#         recur(lines, )
#
#
#     return count

def points_cover_naive(starts, ends, points):
    dic = {}

    for start, end in zip(starts, ends):
        for i in range(start, end + 1):
            dic[i] = dic.get(i, 0) + 1

    count = [0] * len(points)
    for i, point in enumerate(points):
        count[i] = dic.get(point, 0)

    return count


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(points_cover_naive([0, 7], [5, 10], [1, 6, 11]), [1, 0, 0])  # add assertion here
        self.assertEqual(points_cover_naive([1, -2, 3], [1, 5, 5], [3, 5, -2]), [2, 2, 1])


if __name__ == '__main__':
    unittest.main()
