def solution():
    n = int(input())
    x, y = 1, 1
    path = input().split()

    for dir in path:
        if dir == 'R' and y != n:
            y += 1
        elif dir == 'L' and y != 1:
            y -= 1
        elif dir == 'U' and x != 1:
            x -= 1
        elif dir == 'D' and x != n:
            x += 1

    print(x, y)

solution()