def solution():
    steps = [(-2, -1), (-1, -2), (-2, 1), (1, -2), (2, -1), (-1, 2), (2, 1), (1, 2)]
    position = input()
    answer = 0
    row = int(position[1])
    column = int(ord(position[0])) - int(ord('a')) + 1
    for step in steps:
        nRow = row + step[1]
        nColumn = column + step[0]

        if nRow >= 1 and nRow <= 8 and nColumn >= 1 and nColumn <= 8:
            answer += 1

    return answer

print(solution())