n = int(input())
count = 0
answer = 0
while n > 0:
    count += 1
    answer += count
    if n < answer:
        count -= 1
        break

print(count)


# while n > 0:
#     n -= count
#     if n < count: break
#     count += 1