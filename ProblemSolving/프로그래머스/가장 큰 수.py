def solution(numbers):
    numbers = sorted(list(map(str, numbers)), reverse=True, key=lambda x: x * 3)
    return "".join(numbers)
print(solution([6, 10, 2]))