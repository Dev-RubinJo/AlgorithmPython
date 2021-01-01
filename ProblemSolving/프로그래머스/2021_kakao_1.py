import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    if len(new_id) == 0:
        new_id += 'a'
    if new_id[0] == '.':
        new_id = new_id.replace('.', '', 1)
    if len(new_id) != 0 and new_id[len(new_id) - 1] == '.':
        new_id = new_id[:len(new_id) - 1]
    if len(new_id) == 0:
        new_id += 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]

        if new_id[0] == '.':
            new_id = new_id.replace('.', '', 1)
        if len(new_id) != 0 and new_id[len(new_id) - 1] == '.':
            new_id = new_id[:len(new_id) - 1]
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[len(new_id) - 1]
    # print(new_id)
    return new_id
# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
# print(solution(""))
# print(solution("..........."))
print(solution("111.....1.1.1.1.11..1.1."))
# 111.1.1.1.1.11.