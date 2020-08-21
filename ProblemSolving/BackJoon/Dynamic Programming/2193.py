def getRoot(n):
    count = 0
    while(n > 1):
        n /= 2
        count += 1
    return count

def fibo(array, n):
    if n == 0:
        return 0
    if n == 1:
        array[n] = 1
        return 1
    else:
        if array[n] == 0:
            array[n] = fibo(array, n - 1) + fibo(array, n - 2)
        return array[n]

n = int(input())
array = [0] * 91
fibo(array, n)
answer = array[n]
print(answer)