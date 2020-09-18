import sys
input = sys.stdin.readline

tc = int(input().rstrip('\n'))

for _ in range(tc):
    n = int(input().rstrip('\n'))
    pairs = []
    count = 1
    for _ in range(n):
        a, b = map(int, input().rstrip('\n').split())
        pairs.append((a, b))
    pairs.sort()
    a, b = pairs.pop(0)
    for i in pairs:
        if b > i[1]:
            b = i[1]
            count += 1

    print(count)

