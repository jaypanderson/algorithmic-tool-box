'''
just as a reminder the following syntax can be used when you want to access the two values when comparing for a sort as
well as make use of additional variables for the sort.

numbers.sort(key=cmp_to_key(lambda x, y: compare(x, y, z)))

this way you can access the two values directly and then pass in as many variables into your custom compare function.
'''


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
