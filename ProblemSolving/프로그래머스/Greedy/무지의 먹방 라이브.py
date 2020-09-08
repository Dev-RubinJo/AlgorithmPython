'''
뜬금없지만 우선 문제을 보고 처음엔 회전초밥이 떠올랐다
여튼

우선 무지가 음식을 1번부터 먹기 시작하며 1초에 음식을 한번 섭취하고 다음음식으로 넘어간다
먹방을 시작한지 K초가 지나면 라이브 방송이 잠시 끊기는데 다시 시작할 때 어떤 번호부터 시작해야하는지 찾아야한다. <- 이게 답

각 음식의 양을 입력받고 k초를 입력받는다.
음식의 양을 입력받을 때 음식의 순서도 같이 저장이 될 수 있도록 한다.

처음 생각난 방식
food_times_with_order를 food_times의 원소를 기준으로 정렬하고
k가 0이 될때까지 각 횟수를 빼준다.
'''

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    food_times_with_order = []

    for i in range(len(food_times)):
        food_times_with_order.append([food_times[i], i + 1])
    food_times_with_order.sort()
    n = len(food_times)
    pretime = 0
    i = 0
    for f in food_times_with_order:
        diff = f[0] - pretime
        if diff != 0:
            time = diff * n
            if time <= k:
                k -= time
                pretime = f[0]
            else:
                for_sort = []
                not_for_sort = []
                k %= n
                for j in range(0, i):
                    not_for_sort.append(food_times_with_order[j])
                for j in range(i, len(food_times)):
                    for_sort.append(food_times_with_order[j])
                for_sort.sort(key= lambda a: a[1])
                final = not_for_sort + for_sort
                return final[i + k][1]
        i += 1
        n -= 1
    return -1

# print(solution([3, 1, 2], 5))
# print(solution([3,1,1,1,2,4,3],12))
# print(solution([4, 3, 5, 6, 2], 7))
# print(solution([4, 1, 1, 5], 7))
print(solution([946, 314, 757, 322, 559, 647, 983, 482, 145], 1833))