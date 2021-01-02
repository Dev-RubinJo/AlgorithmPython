def test() -> int:
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    result = 0
    while (m > 0):
        for _ in range(0, k):
            if m <= 0:
                break
            result += arr[0]
            m -= 1
        if m <= 0:
            break
        result += arr[1]
        m -= 1
    return result


print(test())


def with_calculate() -> int:
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    count = (m // (k + 1)) * k
    count += m % (k + 1)

    result = count * arr[0]
    result += (m - count) * arr[1]
    return result


print(with_calculate())
