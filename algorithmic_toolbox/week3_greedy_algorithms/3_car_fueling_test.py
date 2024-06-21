import unittest


def min_refills(distance, tank, stops):
    stops.append(distance)
    dist = 0
    prev = None
    refills = 0
    i = 0
    while i < len(stops):
        if prev is None and stops[i] - dist > tank:
            return -1
        elif stops[i] - dist < tank:
            prev = stops[i]
            i += 1
        else:
            if stops[i] - prev > tank:
                return -1
            else:
                dist = prev
                prev = stops[i]
                refills += 1

    return refills


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(min_refills(950, 400, [200, 375, 550, 750]), 2)  # add assertion here
        self.assertEqual(min_refills(10, 3, [1, 2, 5, 9]), -1)  # add assertion here
        self.assertEqual(min_refills(200, 250, [100, 150]), 0)  # add assertion here
        self.assertEqual(min_refills(700, 200, [100, 200, 300, 400]), -1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
