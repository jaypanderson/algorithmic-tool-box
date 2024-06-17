# Uses python3
import sys

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    period = 0

    for _ in range(100):
        previous, current = current, (previous + current)
        period += 1
        if previous % 10 == 0 and current % 10 == 1:
            break

    n %= period

    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        _sum += current

    return _sum % 10


def fibonacci_partial_sum_naive(from_, to):

    return (fibonacci_sum(to) - fibonacci_sum(from_ - 1)) % 10


if __name__ == '__main__':
    #input = sys.stdin.read()
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
