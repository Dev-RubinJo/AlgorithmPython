n = int(input())
array = []
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        array.append([from_pos, to_pos])
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    array.append([from_pos, to_pos])
    hanoi(n - 1, aux_pos, to_pos, from_pos)

hanoi(n, 1, 3, 2)

print(len(array))
for i in array:
    print(i[0], i[1])