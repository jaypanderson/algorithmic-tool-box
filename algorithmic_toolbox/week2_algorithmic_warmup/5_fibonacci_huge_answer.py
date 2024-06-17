"""
this function and the following functions use the fact that there are repeating remainder patterns this pattern is called
pisano period. the cycle restarts when the remainder is 0 and then 1 on the next one.  using this we can calculate the
modulo of huge fibonacci numbers. we can reduce it to the cycle length and then figure out what the last number is.

"""

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
    n %= period

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
