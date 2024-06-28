def change(money):
    dp = [0] * (money + 1)
    coins = [1, 3, 4]
    for i in range(1, len(dp)):
        mini = float('inf')
        for coin in coins:
            temp = i - coin
            if temp >= 0:
                mini = min(mini, dp[temp])
        dp[i] = mini + 1

    return dp[-1]


if __name__ == '__main__':
    m = int(input())
    print(change(m))