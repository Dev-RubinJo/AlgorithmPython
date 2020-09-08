'''
문제를 보면 S = 0001100 일 때
1. 전체를 뒤집으면 1110011 이 된다.
2. 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되서 2번 만에 모두 같은 숫자로 만들 수 있다.
이렇게 설명이 나와있다.

즉 0과 1만 주어지는 상황에서 각각 0으로만, 1로만 바꾸는 횟수를 세고 최소값을 출력하면 된다.
이때 행위를 한번 한다는 의미는 연속된 같은 숫자를 모두 바꿀때 1번으로 카운트한다.
'''
import sys
input = sys.stdin.readline

s = input()
zero = 0
one = 0

if s[0] == '1':
    one += 1
else:
    zero += 1

for i in range(1, len(s) - 1):
    if s[i - 1] != s[i]:
        if s[i] == '1':
            one += 1
        else:
            zero += 1
print(min(one, zero))