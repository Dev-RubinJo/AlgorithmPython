"""
총 학생 명수와 각 학생의 1 ~ 5학년까지의 반을 입력 받고
각 학생별로 학년별 겹치는 반이 있는 인원의 수가 최대인 학생이 임시 반장이 되도록 한다

입력 조건이 학생 수: 3 ~ 1000, 학년은 총 5학년까지 있다.
각 학생별로 겹치는 학생수를 구하기 위해
학생수 만큼 for문을 돌면서 학생을 또 반마다 돌면서 다른학생과 겹치는 학생이 있는지 검사하며 겹친다면
겹치는 학생의 번호를 따로 저장하고 겹치는 횟수를 추가한다
"""

import sys
input = sys.stdin.readline
num = int(input())

students = []
for _ in range(num):
    students.append(list(map(int, input().split())))
best = []
for i in range(num):
    best.append(0)
    check = []
    for j in range(5):
        for k in range(num):
            if i == k:
                continue
            if students[k][j] == students[i][j] and k not in check:
                best[i] += 1
                check.append(k)
max = -1
index = -1
for i in range(len(best)):
    if max < best[i]:
        max = best[i]
        index = i

# print(best)
print(index + 1)