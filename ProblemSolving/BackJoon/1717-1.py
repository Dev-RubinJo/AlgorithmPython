import sys
sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()

def find_parent(target):
    if target == parent[target]:
        return target
    parent[target] = find_parent(parent[target])
    return parent[target]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag:
        print("YES" if find_parent(a) == find_parent(b) else "NO")
    else:
        union(a, b)