import sys
input = sys.stdin.readline

num = input()

zero = 0
one = 0

if int(num[0]) == 0:
    zero += 1
else:
    one += 1

for i in range(1, len(num) - 1):
    if int(num[i - 1]) == 0 and int(num[i]) == 1:
        one += 1
    elif int(num[i - 1]) == 1 and int(num[i]) == 0:
        zero += 1
print(min(one, zero))