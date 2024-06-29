def edit_distance(first_string, second_string):
    dp = [[0 for _ in range(len(first_string) + 1)] for _ in range(len(second_string) + 1)]
    for i in range(len(first_string) + 1):
        dp[0][i] = i
    for i in range(len(second_string) + 1):
        dp[i][0] = i

    for i in range(1, len(second_string) + 1):
        for j in range(1, len(first_string) + 1):
            temp = [dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1]]
            if second_string[i - 1] != first_string[j-1]:
                temp[-1] += 1
            dp[i][j] = min(temp)

    return dp[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
