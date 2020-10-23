import sys
input = sys.stdin.readline

t = int(input().rstrip('\n'))
a_len = int(input().rstrip('\n'))
a = list(map(int, input().rstrip('\n').split()))
b_len = int(input().rstrip('\n'))
b = list(map(int, input().rstrip('\n').split()))

a_sum = dict()
b_sum = dict()

for i in range(a_len):
    key = 0
    for j in range(i, a_len):
        key += a[j]
        if a_sum.get(key):
            a_sum[key] += 1
        else:
            a_sum[key] = 1

for i in range(b_len):
    key = 0
    for j in range(i, b_len):
        key += b[j]
        if b_sum.get(key):
            b_sum[key] += 1
        else:
            b_sum[key] = 1

answer = 0
for c, (k, v) in enumerate(a_sum.items()):
    if b_sum.get(t - k):
        answer += (a_sum[k] * b_sum[t - k])
print(answer)