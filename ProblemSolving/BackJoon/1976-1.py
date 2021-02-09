def parent_find(parent, x):
    if x == parent[x]:
        return x
    p = parent_find(parent, parent[x])
    parent[x] = p
    return parent[x]


def union(parent, x, y):
    x = parent_find(parent, x)
    y = parent_find(parent, y)
    if x != y:
        parent[y] = x
def solution1976():
    cities = int(input())
    _ = int(input())
    parent = {i: i for i in range(1, cities + 1)}

    for y in range(1, cities + 1):
        maps = list(map(int, input().split()))
        for x in range(1, len(maps) + 1):
            if maps[x - 1] == 1:
                union(parent, y, x)

    tour = list(map(int, input().split()))
    result = set([parent_find(parent, i) for i in tour])
    print("YES" if len(result) == 1 else print("NO"))

solution1976()