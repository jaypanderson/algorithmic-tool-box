def gcd(a, b):
    while a != 0 and b != 0:
        if a < b:
            b = b % a
        else:
            a %= b

    return max(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
