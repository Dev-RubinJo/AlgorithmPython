import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().rstrip('\n').split())
    if n == 0 and m == 0:
        break
    call_case = []
    police_case = []

    for _ in range(n):
        call_case.append(list(map(int, input().rstrip('\n').split()))) # Source, Desination, Start(시작시간), Duration(통화 시간)
    for _ in range(m):
        police_case.append(list(map(int, input().rstrip('\n').split())))
    for police in police_case:
        count = 0
        for call in call_case:
            if call[2] < police[0] + police[1] and police[0] < call[2] + call[3]:
                count += 1
        print(count)