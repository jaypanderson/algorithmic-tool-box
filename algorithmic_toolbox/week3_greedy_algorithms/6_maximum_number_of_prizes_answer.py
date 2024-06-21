def optimal_summands(n):
    summands = [1]
    total = 1
    remain = n - 1
    while total < n:
        new = summands[-1] + 1
        if remain < new:
            summands[-1] += remain
            break
        summands.append(new)
        total += new
        remain -= new
        #print('total: ', total)

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
