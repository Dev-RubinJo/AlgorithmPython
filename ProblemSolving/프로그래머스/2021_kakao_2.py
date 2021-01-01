from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        for j in orders:
            a = list(combinations(j, i))
            for k in a: # 각 조합에 대해
                result = ""
                count = 0
                isThere = []
                for l in orders: #순서 배열의 각 문자열마다
                    if l == j:
                        continue
                    for let in k: # k조합의 글자가
                        if let not in l: # 문자열 안에 없다면
                            isThere.append(False)
                            break
                    if False in isThere:
                        break
                    else:
                        count += 1
                    if count > 0:
                        for let in k:
                            result += let
                    if result != "" and result not in answer:
                        answer.append(result)
                        result = ""

    print(set(answer))
    return set(answer)




# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["XYZ", "XWY", "WXA"], [2,3,4])