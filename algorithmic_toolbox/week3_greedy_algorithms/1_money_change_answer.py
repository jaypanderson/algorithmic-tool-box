def change(money):
    denoms = [10, 5, 1]
    coins = 0
    for denom in denoms:
        coins += money // denom
        money %= denom

    return coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
