import sys
input = sys.stdin.readline
n = int(input().rstrip('\n'))
files = []
for _ in range(n):
    files.append(input().rstrip('\n'))
answer = dict()
for i in range(n):
    index = files[i].find('.')
    # print(files[i][index+1:])
    if answer.get(files[i][index+1:]):
        answer[files[i][index+1:]] += 1
    else:
        answer[files[i][index + 1:]] = 1
answer = sorted(answer.items())
for key, value in answer:
    print(key, value)
