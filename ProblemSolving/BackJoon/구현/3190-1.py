'''
사과의 위치는 1
뱀의 위치는 2
그 지렁이 게임을 하는 것처럼 구현을 해봤다.
'''
n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

l = int(input())
direction = []
for _ in range(l):
    a, b = input().split()
    direction.append((int(a), b))

def change_direction(now, direction):
    if direction == 'L':
        index = (now - 1) % 4
        return index
    else:
        index = (now + 1) % 4
        return index
d = 0
snake = [(1, 1)]
board[1][1] = 2
flag = False
time = 0
i = 0
while True:
    nx, ny = snake[len(snake) - 1][0] + dx[d], snake[len(snake) - 1][1] + dy[d]
    if nx > 0 and nx <= n and ny > 0 and ny <= n and board[nx][ny] != 2:
        if board[nx][ny] == 1:
            snake.append((nx, ny))
            board[nx][ny] = 2
        elif board[nx][ny] == 0:
            snake.append((nx, ny))
            to_delete = snake.pop(0)
            board[to_delete[0]][to_delete[1]] = 0
            board[nx][ny] = 2
    else:
        time += 1
        break
    time += 1
    if i < l and time == direction[i][0]:
        d = change_direction(d, direction[i][1])
        i += 1
print(time)