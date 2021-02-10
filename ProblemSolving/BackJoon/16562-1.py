import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x, store, check, adj):
    check[x] = True
    for i in adj[x]:
        if check[i] == False:
            store.append(i)
            dfs(i, store, check, adj)
    return store

def solution16562():
    n, m, k = map(int, input().rstrip('\n').split())
    moneys = list(map(int, input().rstrip('\n').split()))
    adj = [[] for _ in range(n)]
    ans = []
    for i in range(m):
        a, b = map(int, input().rstrip('\n').split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    check = [False for _ in range(n)]

    for i in range(n):
        if check[i] == False:
            each = dfs(i, [i], check, adj)
            temp = 999999999999999
            for j in each:
                if temp > moneys[j]:
                    temp = moneys[j]
            ans.append(temp)
    print(sum(ans) if sum(ans) <= k else "Oh no")
solution16562()