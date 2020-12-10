# def solution(N, stages):
#     answer = []
#     stages.sort()
#     stage = []
#     pivot = 1
#     count = 0
#     pass_count = 0
#     for i in range(len(stages)):
#         if stages[i] == pivot:
#             count += 1
#         if i == len(stages) - 1:
#             stage.append((pivot, count / (len(stages) - pass_count)))
#             break
#         elif stages[i + 1] > pivot:
#             if count == 0:
#                 stage.append((pivot, 0.0))
#             else:
#                 stage.append((pivot, count / (len(stages) - pass_count)))
#             pass_count += count
#             count = 0
#             pivot += 1
#     stage.sort(key=lambda x: -x[1])
#     for a, b in stage:
#         answer.append(a)
#     return answer

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count
    answer = sorted(answer, key=lambda t: -t[1])
    answer = [i[0] for i in answer]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4, 4, 4, 4, 4]))
# print(solution(8, [1, 2, 3, 4, 5, 6, 7]))