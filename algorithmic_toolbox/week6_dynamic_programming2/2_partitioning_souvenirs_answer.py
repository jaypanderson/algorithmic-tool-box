from sys import stdin


def can_partition(values, n, subset_sum, subset_sums, taken, target_sum):
    if subset_sums[0] == target_sum and subset_sums[1] == target_sum:
        return True

    for i in range(n):
        if taken[i]:
            continue
        temp_sum = subset_sums.copy()
        for j in range(3):
            if subset_sums[j] + values[i] <= target_sum:
                taken[i] = True
                subset_sums[j] += values[i]
                if can_partition(values, n, subset_sum, subset_sums, taken, target_sum):
                    return True
                taken[i] = False
                subset_sums = temp_sum
    return False

def partition3(values):
    n = len(values)
    if n < 3:
        return 0
    total_sum = sum(values)
    if total_sum % 3 != 0:
        return 0
    target_sum = total_sum // 3
    subset_sums = [0] * 3
    taken = [False] * n
    return 1 if can_partition(values, n, target_sum, subset_sums, taken, target_sum) else 0



if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))