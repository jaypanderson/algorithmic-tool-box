import unittest


def optimal_value(capacity, weights, values):
    max_val = 0
    pairs = [[value, weight] for value, weight in zip(values, weights)]
    pairs.sort(reverse=True, key=lambda x: x[0] / x[1])
    for value, weight in pairs:
        if capacity > weight:
            capacity -= weight
            max_val += value
        else:
            frac = capacity / weight
            max_val += value * frac
            break

    return round(max_val, 4)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(optimal_value(50, [20, 50, 30], [60, 100, 120]), 180.0)
        self.assertEqual(optimal_value(10, [30], [500]), 166.6667)# add assertion here


if __name__ == '__main__':
    unittest.main()
