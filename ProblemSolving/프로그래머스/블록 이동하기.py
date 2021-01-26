from collections import deque

def get_next_position(position, board):
    next = []
    position = list(position)
    position1_x, position1_y, position2_x, position2_y = position[0][0], position[0][1], position[1][0], position[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        next1_x, next1_y, next2_x, next2_y = position1_x + dx[i], position1_y + dy[i], position2_x + dx[i], position2_y + dy[i]
        if board[next1_x][next1_y] == 0 and board[next2_x][next2_y] == 0:
            next.append({(next1_x, next1_y), (next2_x, next2_y)})
    if position1_x == position2_x:
        for i in [-1, 1]:
            if board[position1_x + i][position1_y] == 0 and board[position2_x + i][position2_y] == 0:
                next.append({(position1_x, position1_y), (position1_x + i, position1_y)})
                next.append({(position2_x, position2_y), (position2_x + i, position2_y)})
    elif position1_y == position2_y:
        for i in [-1, 1]:
            if board[position1_x][position1_y + i] == 0 and board[position2_x][position2_y + i] == 0:
                next.append({(position1_x, position1_y), (position1_x, position1_y + i)})
                next.append({(position2_x, position2_y), (position2_x, position2_y + i)})

    return next

def solution(board):
    n = len(board)
    new = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new[i + 1][j + 1] = board[i][j]
    q = deque()
    visited = []
    position = {(1, 1), (1, 2)}

    q.append((position, 0))
    visited.append(position)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_position in get_next_position(pos, new):
            if next_position not in visited:
                q.append((next_position, cost + 1))
                visited.append(next_position)
    return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))