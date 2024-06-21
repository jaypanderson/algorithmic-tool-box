def optimal_summands(n):
    summands = [1]
    total = 1
    while total < n:
        new = summands[-1] + 1
        summands.append(new)
        total += new
        #print('total: ', total)

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
