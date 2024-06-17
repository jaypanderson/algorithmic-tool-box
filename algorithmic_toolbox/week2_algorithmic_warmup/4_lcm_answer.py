def gcd(a, b):
    while a != 0 and b != 0:
        #print(a, b)
        if a < b:
            b %= a
        else:
            a %= b

    return max(a, b)

def lcm(a, b):
    d = gcd(a, b)
    return (a*b) // d


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))