from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    first_sequence.sort()
    second_sequence.sort()

    return sum([one * two for one, two in zip(first_sequence, second_sequence)])


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

