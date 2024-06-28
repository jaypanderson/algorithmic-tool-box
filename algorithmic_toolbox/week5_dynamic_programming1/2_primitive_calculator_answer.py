def compute_operations(n):
    dp = [0] * (n + 1)
    ops = [[], []]
    operators = [['1', '-'], ['2', '/'], ['3', '/']]
    for i in range(2, n + 1):
        mini = float('inf')
        cur_op = None
        for num, op in operators:
            temp = eval(str(i) + op + num)
            if temp >= 0 and temp == int(temp) and dp[int(temp)] < mini:
                mini = dp[int(temp)]
                cur_op = [num, op]
        ops.append(cur_op)
        dp[i] = mini + 1

    cur = n
    ans = [n]
    while ops[cur]:
        num, op = ops[cur]
        cur = int(eval(str(cur) + op + num))
        ans.append(cur)

    return ans[::-1]

# [[0, 1], [,]]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)


    # dp = [n]
    # while n >= 2:
    #     if n % 3 == 0:
    #         n //= 3
    #     elif n % 3 == 1:
    #         n -= 1
    #     elif n % 2 == 0:
    #         n //= 2
    #     else:
    #          n -= 1
    #     dp.append(n)
    # return dp[::-1]