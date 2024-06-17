def fibonacci_number(n):
    ans = [0, 1]
    if n < 2:
        return ans[n]
    for n in range(n-1):
        ans.append(ans[-1] + ans[-2])
    return ans[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
