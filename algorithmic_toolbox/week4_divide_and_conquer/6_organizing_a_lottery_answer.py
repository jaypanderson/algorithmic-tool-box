from sys import stdin


def points_cover_naive(starts, ends, points):
    dic = {}

    for start, end in zip(starts, ends):
        for i in range(start, end + 1):
            dic[i] = dic.get(i, 0) + 1

    count = [0] * len(points)
    for i, point in enumerate(points):
        count[i] = dic.get(point, 0)

    return count


    # assert len(starts) == len(ends)
    # count = [0] * len(points)
    #
    # for index, point in enumerate(points):
    #     for start, end in zip(starts, ends):
    #         if start <= point <= end:
    #             count[index] += 1


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)
