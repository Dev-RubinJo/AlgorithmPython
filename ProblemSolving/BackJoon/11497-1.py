def solution11497():
    t = int(input())
    for _ in range(t):
        n = int(input())
        sorted_logs = [0 for _ in range(n + 1)]
        logs = list(map(int, input().split()))
        logs.sort()

        front_index = 0
        rear_index = n - 1
        for i in range(n):
            if i % 2 == 0:
                sorted_logs[front_index] = logs[i]
                front_index += 1
            else:
                sorted_logs[rear_index] = logs[i]
                rear_index -= 1
        sorted_logs[n] = sorted_logs[0]
        result = 0
        for i in range(n):
            result = max(result, abs(sorted_logs[i] - sorted_logs[i + 1]))
        print(result)
    return
solution11497()