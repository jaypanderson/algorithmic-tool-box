import unittest


def min_refills(distance, tank, stops):
    stops.append(distance)
    cur = 0
    prev = None
    refills = 0
    for stop in stops:
        if prev is None and stop - cur > tank:
            return -1
        elif stop - cur > tank:
            cur = prev
            prev = None
            refills += 1
        else:
            prev = stop

    return refills


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(min_refills(950, 400, [200, 375, 550, 750]), 2)  # add assertion here
        self.assertEqual(min_refills(10, 3, [1, 2, 5, 9]), -1)  # add assertion here
        self.assertEqual(min_refills(200, 250, [100, 150]), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
