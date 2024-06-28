def compute_operations(n):
    dp = [n]
    operators = [['1', '-'], ['2', '/'], ['3', '/']]
    while n >= 2:
        if n % 3 == 0:
            n //= 3
        elif n % 3 == 1:
            n -= 1
        elif n % 2 == 0:
            n //= 2
        else:
             n -= 1
        dp.append(n)
    return dp[::-1]










    # for i in range(2, len(dp)):
    #     mini = float('inf')
    #     for num, op in operators:
    #         temp = eval(str(i) + op + num)
    #         if temp >= 0 and temp == int(temp):
    #             mini = min(mini, dp[int(temp) - 1])
    #     dp[i] = mini + 1

    # return dp

# [[0, 1], [,]]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
