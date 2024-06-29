import unittest


def maximum_gold(capacity, weights):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = dp[i-1][j]
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i][j], dp[i-1][j - weights[i-1]] + weights[i-1])

    return dp[n][capacity]




class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(maximum_gold(10, [1, 4, 8]), 9)  # add assertion here


if __name__ == '__main__':
    unittest.main()
