from sys import stdin


def min_refills(distance, tank, stops):
    stops.append(distance)
    cur = 0
    prev = None
    refills = 0
    for stop in stops:
        if prev is None and stop - cur > tank:
            return -1
        elif stop - cur > tank:
            cur = prev
            prev = None
            refills += 1
        else:
            prev = stop

    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
