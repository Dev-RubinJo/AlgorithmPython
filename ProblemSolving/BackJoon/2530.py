def solution():
    h, m, s = map(int, input().split())
    time = int(input())
    s += time
    m += s / 60; s %= 60
    h += m / 60; m %= 60
    h %= 24
    print(int(h), int(m), int(s))
    return
solution()