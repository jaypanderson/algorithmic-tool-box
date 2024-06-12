import unittest
from max_pairwise_product_answer import max_pairwise_product, max_pairwise_product_n


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tests = [[[10, 9], 90],
                 [[10, 9, 8], 90],
                 [[1,2,3,4], 12]]
        for arg, ans in tests:
            self.assertEqual(max_pairwise_product(arg), ans)  # add assertion here

    def test_lengthly_input(self):
        arg = [x for x in range(10000000)]
        ans = 99999970000002
        self.assertEqual(max_pairwise_product(arg), ans)

    def test_negative_input(self):
        arg = [-1, -2, -3, -4]
        ans = 12
        self.assertEqual(max_pairwise_product(arg), ans)

    def test_negative_input_2(self):
        arg = [-1, 2, 3, 4]
        ans = 12
        self.assertEqual(max_pairwise_product(arg), ans)

    def test_negative_input_3(self):
        arg = [-1, -2, 3, 4]
        ans = 12
        self.assertEqual(max_pairwise_product(arg), ans)

    def test_n_time_function(self):
        arg = [x for x in range(10000000)]
        ans = 99999970000002
        self.assertEqual(max_pairwise_product_n(arg), ans)

if __name__ == '__main__':
    unittest.main()
