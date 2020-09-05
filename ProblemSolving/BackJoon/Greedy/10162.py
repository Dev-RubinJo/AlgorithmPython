t = int(input())
a = 0 # 300
b = 0 # 60
c = 0 # 10

if t // 300 > 0:
    a = t // 300
    t %= 300
if t // 60 > 0:
    b = t // 60
    t %= 60
if t // 10 > 0:
    c = t // 10
    t %= 10
if t != 0:
    print(-1)
else:
    print(a, b, c)