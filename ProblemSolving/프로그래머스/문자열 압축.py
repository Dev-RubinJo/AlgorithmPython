def solution(s):
    answer = len(s)
    for check in range(1, len(s) // 2 + 1):
        temp = ""
        toCheck = s[0: check]
        count = 1 # toCheck count
        for i in range(check, len(s), check):
            if toCheck == s[i: i + check]:
                count += 1
            else:
                temp += str(count) + toCheck if count >= 2 else toCheck
                toCheck = s[i: i + check]
                count = 1
        temp += str(count) + toCheck if count >= 2 else toCheck
        answer = min(answer, len(temp))
    return answer
