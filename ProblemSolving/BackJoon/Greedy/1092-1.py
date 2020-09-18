import sys
input = sys.stdin.readline
n = int(input().rstrip('\n'))
limit_weight = list(map(int, input().rstrip('\n').split()))
num_of_box = int(input().rstrip('\n'))
weight_of_box = list(map(int, input().rstrip('\n').split()))

limit_weight.sort(reverse=True)
weight_of_box.sort(reverse=True)
answer = 0
if limit_weight[0] < weight_of_box[0]:
    print(-1)
else:
    while True:
        answer += 1
        for i in range(n):
            for j in range(len(weight_of_box)):
                if limit_weight[i] >= weight_of_box[j]:
                    weight_of_box.pop(j)
                    break
        if len(weight_of_box) == 0:
            break
    print(answer)