def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    period = 0

    for _ in range(m**2):
        previous, current = current, (previous + current)
        period += 1
        if previous % m == 0 and current % m == 1:
            break
    print('period: ', period)
    n %= period
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
