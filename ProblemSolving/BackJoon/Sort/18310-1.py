import sys
input = sys.stdin.readline

n = int(input().rstrip('\n'))
locations = list(map(int, input().rstrip('\n').split()))
locations.sort()
print(locations[(n - 1) // 2])