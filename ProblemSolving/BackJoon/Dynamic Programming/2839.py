n = int(input())

def sugar(n):
    for y in range((n // 3) + 1):
        for x in range((n // 5) + 1):
            if ((5 * x + 3 * y) == n):
                return x + y

    return -1

count = sugar(n)
print(count)