from sys import stdin


def optimal_value(capacity, weights, values):
    max_val = 0
    pairs = [[value, weight] for value, weight in zip(values, weights)]
    pairs.sort(reverse=True, key=lambda x: x[0] / x[1])
    for value, weight in pairs:
        if capacity > weight:
            capacity -= weight
            max_val += value
        else:
            frac = capacity / weight
            max_val += value * frac
            break

    return round(max_val, 4)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
