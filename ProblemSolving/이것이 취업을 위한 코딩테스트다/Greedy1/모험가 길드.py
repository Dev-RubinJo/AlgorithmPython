n = int(input())
scarce_levels = map(int, input().split())
count = 0

scarce_levels = sorted(scarce_levels, reverse=True)

while scarce_levels:
    large_num = scarce_levels[0]
    count += 1
    for _ in range(large_num):
        scarce_levels.remove(scarce_levels[0])


print(count)
