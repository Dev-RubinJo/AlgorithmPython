def worst_solution():
    n = int(input())
    components = list(map(int, input().split()))
    m = int(input())
    components_to_find = list(map(int, input().split()))
    answer = []
    check = False
    for i in range(m):
        for j in range(n):
            if components_to_find[i] == components[j]:
                answer.append("yes")
                check = True
                break
        if check != True:
            answer.append("no")

    for ans in answer:
        print(ans, end=' ')


def binary_search(array, target, start, end):
    while start <= end:
        mid = int((start + end) / 2)

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def binary_solution():
    n = int(input())
    components = list(map(int, input().split()))
    components.sort()
    m = int(input())
    components_to_find = list(map(int, input().split()))

    for i in components_to_find:
        result = binary_search(components, i, 0, n - 1)
        if result == None:
            print("no", end=' ')
        else:
            print("yes", end=' ')
