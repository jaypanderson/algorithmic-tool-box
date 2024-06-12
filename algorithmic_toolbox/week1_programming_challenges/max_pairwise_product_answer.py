def max_pairwise_product(numbers):
    numbers.sort()
    neg = 0
    for num in numbers:
        if num < 0:
            neg += 1

    maxi = float('-inf')
    if neg >= 2:
        maxi = max((numbers[0] * numbers[1]), maxi)

    return max((numbers[-1] * numbers[-2]), maxi)


def max_pairwise_product_n(numbers: list[int]) -> int:
    """
    this implementation is big O(n) comapred to the nlogn solution above. This is done by passing by the list to find
    the two largest numbers. the text suggests doing thing by doing two passed over the list but it can be done in a
    single pass
    :param numbers:
    :return:
    """
    first = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > first:
            second = first
            first = num
    return first * second


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
