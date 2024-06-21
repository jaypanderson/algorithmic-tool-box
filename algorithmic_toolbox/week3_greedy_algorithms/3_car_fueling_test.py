import unittest


def min_refills(distance, tank, stops):
    stops.append(distance)
    if stops[0] > tank:
        return -1
    refills = 0
    cur = tank
    for i, stop in enumerate(stops):
        if stop > cur:
            if stop > tank + stops[i-1]:
                return -1
            cur = stops[i-1] + tank
            refills += 1

    return refills


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(min_refills(950, 400, [200, 375, 550, 750]), 2)  # add assertion here
        self.assertEqual(min_refills(10, 3, [1, 2, 5, 9]), -1)  # add assertion here
        self.assertEqual(min_refills(200, 250, [100, 150]), 0)  # add assertion here
        self.assertEqual(min_refills(700, 200, [100, 200, 300, 400]), -1)  # add assertion here
        self.assertEqual(min_refills(500, 200, [100, 200, 300, 400]), 2)  # add assertion here



if __name__ == '__main__':
    unittest.main()
