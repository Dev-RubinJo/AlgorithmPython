def test():
    n, m = map(int, input().split())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
        arr[i].sort()
    max = 0
    for i in range(n):
        if max < arr[i][0]:
            max = arr[i][0]
    return max

def solution():
    n, m = map(int, input().split())
    result = 0
    for _ in range(n):
        arr = list(map(int, input().split()))
        min_value = min(arr)
        result = max(min_value, result)
    return result

print(solution())