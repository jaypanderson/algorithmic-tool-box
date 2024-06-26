from itertools import combinations
from collections import deque


def merge_sort(nums, inversions):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = deque(merge_sort(nums[:mid], inversions))
    right = deque(merge_sort(nums[mid:], inversions))
    new = []
    while left and right:
        if left[0] <= right[0]:
            new.append(left.popleft())
        else:
            inversions[0] += len(left)
            new.append((right.popleft()))
    return new + list(left) + list(right)


def inversions_naive(nums):
    inversions = [0]
    merge_sort(nums, inversions)
    return inversions[0]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
