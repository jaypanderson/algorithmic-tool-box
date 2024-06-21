from sys import stdin


def min_refills(distance, tank, stops):
    stops.append(distance)
    if stops[0] > tank:
        return -1
    refills = 0
    cur = tank
    for i, stop in enumerate(stops):
        if stop > cur and stop > tank + stops[i-1]:
            return -1
        elif stop > cur:
            cur = stops[i-1] + tank
            refills += 1

    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
