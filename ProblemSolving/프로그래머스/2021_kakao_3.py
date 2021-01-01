def solution(info, query):
    info_list = []
    query_list = []
    total = []
    for i in info:
        info_list.append(i.split(' '))
    for i in query:
        query_list.append(i.replace("and ", "").replace("-", "any").split(' '))
    for q in query_list:
        count = 0
        for i in info_list:
            if (q[0] == "any" or q[0] == i[0]) and (q[1] == "any" or q[1] == i[1]) and (q[2] == "any" or q[2] == i[2]) and (q[3] == "any" or q[3] == i[3]) and (int(i[4]) >= int(q[4])):
                count += 1
            # flag = True
            # for j in range(5):
            #     if q[j] == "any":
            #         continue
            #     if j == 4 and int(i[j]) < int(q[len(q) - 1]):
            #         flag = False
            #         break
            #     if i[j] not in q and j != 4:
            #         flag = False
            #         break
            # if flag:
            #     count += 1
        total.append(count)


    return total

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])