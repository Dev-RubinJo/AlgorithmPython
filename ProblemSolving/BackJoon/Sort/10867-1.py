import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
unsorted_list = list(map(int, input().rstrip('\n').split()))


def quick_sort(prm_list):
    length = len(prm_list)
    if length < 2:
        return prm_list
    lesser = []
    greater = []

    pivot = prm_list.pop(0)

    for i in prm_list:
        if i < pivot:
            lesser.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            continue

    lesser = quick_sort(lesser)
    greater = quick_sort(greater)

    lesser.append(pivot)
    ans = lesser + greater

    return ans

for i in quick_sort(unsorted_list):
    print(i, end=' ')