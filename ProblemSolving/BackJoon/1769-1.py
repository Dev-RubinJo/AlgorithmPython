import sys
input = sys.stdin.readline

def solution1769():
    number = input().rstrip('\n')
    count = 0

    while (len(number) > 1):
        temp = 0
        for i in range(len(number)):
            temp += int(number[i])
        number = str(temp)
        count += 1
    print(count)
    print("YES" if int(number) % 3 == 0 else "NO")
solution1769()