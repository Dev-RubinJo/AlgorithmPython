import time

start = time.time()
array = [0] * 100000

def fibo(x):
    if x == 1 or x == 2:
        array[x] = 1
        return array[x]
    if array[x] != 0:
        return array[x]
    array[x] = fibo(x - 1) + fibo(x - 2)
    return array[x]

print(fibo(100))
end = time.time()

print(end - start)