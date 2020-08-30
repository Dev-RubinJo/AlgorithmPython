def rotate90(a):
    n = len(a)
    m = len(a[0])
    result = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(lock):
    length = len(lock) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    newLock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            newLock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        newLock[x + i][y + j] += key[i][j]
                if check(newLock):
                    return True
                for i in range(m):
                    for j in range(m):
                        newLock[x + i][y + j] -= key[i][j]
    return False

    # return answer

n = [[0, 0, 0],
     [1, 0, 0],
     [0, 1, 1]]
m = [[1, 1, 1],
     [1, 1, 0],
     [1, 0, 1]]
print(solution(n, m))