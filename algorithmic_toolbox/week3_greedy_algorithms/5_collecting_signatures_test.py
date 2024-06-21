import unittest


def optimal_points(segments):
    segments.sort(key=lambda x: x[1], reverse=True)
    points = []

    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    while segments:
        cur = segments.pop()[1]
        points.append(cur)
        temp = segments
        segments = []
        for i, seg in enumerate(temp):
            if seg[0] <= cur <= seg[1]:
                continue
            else:
                segments.append(seg)

    return points


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(optimal_points([[1, 3], [2, 5], [3, 6]]), [3])  # add assertion here
        self.assertEqual(optimal_points([[4, 7], [1, 3], [2, 5], [5, 6]]), [3, 6])

if __name__ == '__main__':
    unittest.main()
