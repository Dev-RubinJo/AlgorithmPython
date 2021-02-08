def get_parent(parent, x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent, parent[x])
    return  parent[x]

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b: return 1
    else: return 0

def solution1976():
    n = int(input())
    m = int(input())
    city = [i for i in range(n)]

    for i in range(n):
        city_arr = list(map(int, input().split()))
        for j in range(n):
            if city_arr[j] == 1:
                union_parent(city, i, j)
    tour = list(map(int, input().split()))
    result = set([get_parent(city, i - 1) for i in tour])
    print("YES" if len(result) == 1 else print("NO"))

solution1976()
