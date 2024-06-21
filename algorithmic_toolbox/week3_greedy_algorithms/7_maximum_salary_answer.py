from functools import cmp_to_key


def compare(num_1, num_2):
    if num_1 + num_2 < num_2 + num_1:
        return -1
    elif num_1 + num_2 > num_2 + num_1:
        return 1
    else:
        return 0


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=cmp_to_key(compare), reverse=True)

    return ''.join(numbers)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
