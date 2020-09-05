import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, colors, start, color):
    colors[start] = color
    for i in graph[start]:
        if colors[i] == 0:
            if dfs(graph, colors, i, -color) is False:
                return False
        elif colors[i] == colors[start]:
            return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    colors = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = True
    for i in range(1, v + 1):
        if colors[i] == 0:
            if dfs(graph, colors, i, 1) is False:
                answer = False
                break
    if answer:
        print("YES")
    else:
        print("NO")
























# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline
# k = int(input())
#
# def dfs(graph, start, colors, color):
#     colors[start] = color
#     for i in graph[start]:
#         if colors[i] == 0:
#             if dfs(graph, i, colors, -color) is False:
#                 return False
#         elif colors[i] == colors[start]:
#             return False
#     return True
#
#
# for _ in range(k):
#     v, e = map(int, input().split())
#     graph = [[] for _ in range(v + 1)]
#
#     colors = [0] * (v + 1)
#     for _ in range(e):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     ans = True
#
#     for i in range(1, v + 1):
#         if colors[i] == 0:
#             if dfs(graph, i, colors, 1) is False:
#                 ans = False
#                 break
#
#     if ans:
#         print("YES")
#     else:
#         print("NO")
