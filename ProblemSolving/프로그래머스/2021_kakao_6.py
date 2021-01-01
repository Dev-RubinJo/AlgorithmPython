dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(board, r, c):
    answer = 0
    now = [(r, c)]
    if board[r][c] != 0:
        answer += 1


    return answer


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
