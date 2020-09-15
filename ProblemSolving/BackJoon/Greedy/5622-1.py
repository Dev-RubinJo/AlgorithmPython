def solution(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'B' or s[i] == 'C':
            count += 3
        elif s[i] == 'D' or s[i] == 'E' or s[i] == 'F':
            count += 4
        elif s[i] == 'G' or s[i] == 'H' or s[i] == 'I':
            count += 5
        elif s[i] == 'J' or s[i] == 'K' or s[i] == 'L':
            count += 6
        elif s[i] == 'M' or s[i] == 'N' or s[i] == 'O':
            count += 7
        elif s[i] == 'P' or s[i] == 'Q' or s[i] == 'R' or s[i] == 'S':
            count += 8
        elif s[i] == 'T' or s[i] == 'U' or s[i] == 'V':
            count += 9
        elif s[i] == 'W' or s[i] == 'X' or s[i] == 'Y' or s[i] == 'Z':
            count += 10
        else:
            count += 11
    return count


s = input()
print(solution(s))

print(solution('UNUCIC'))