def solution_worng(n, lost, reserve):
    answer = 0
    answer2 = 0
    take = []
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in range(n):
        if i + 1 in set_reserve:
            take.append(1)
            answer += 1
            answer2 += 1
        elif i + 1 in set_lost:
            take.append(0)
        else:
            take.append(0)
            answer += 1
            answer2 += 1

    for i in range(n):
        if i + 1 in set_lost:
            if i - 1 >= 0 and take[i - 1] == 1:
                answer += 1
    for i in range(n - 1, -1, -1):
        if i in set_lost:
            if take[i] == 1:
                answer2 += 1

    return max(answer, answer2)

def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

print(solution(n, lost, reserve))
