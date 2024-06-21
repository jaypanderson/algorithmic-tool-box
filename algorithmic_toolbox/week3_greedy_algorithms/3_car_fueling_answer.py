from sys import stdin


def min_refills(distance, tank, stops):
    stops.append(distance)
    dist = 0
    prev = None
    refills = 0
    i = 0
    while i < len(stops):
        if prev is None and stops[i] - dist > tank:
            return -1
        elif stops[i] - dist <= tank:
            prev = stops[i]
            i += 1
        else:
            if stops[i] - prev > tank:
                return -1
            else:
                dist = prev
                prev = stops[i]
                refills += 1

    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
