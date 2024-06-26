from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key=lambda x: x[1], reverse=True)
    points = []

    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    while segments:
        cur = segments.pop()[1]
        points.append(cur)
        temp = segments
        segments = []
        for i, seg in enumerate(temp):
            if seg[0] <= cur <= seg[1]:
                continue
            else:
                segments.append(seg)

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
