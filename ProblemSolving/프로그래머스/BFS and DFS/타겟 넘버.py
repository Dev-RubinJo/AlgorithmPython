def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j + i)
            sub.append(j - i)
        sup = sub
    return sup.count(target)

from collections import deque

def solution_BFS(numbers, target):
    answer = 0
    queue = deque([(0, 0)])
    while queue:
        total, index = queue.popleft()
        if index == len(numbers):
            if total == target:
                answer += 1
        else:
            number = numbers[index]
            queue.append((total + number, index + 1))
            queue.append((total - number, index + 1))
    return answer

print(solution_BFS([1, 1, 1, 1, 1], 3))

