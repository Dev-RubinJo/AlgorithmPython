import time

start = time.time()

array = [0] * 100000
array[0] = 0
array[1] = 1
array[2] = 1

n = 100
for i in range(3, n + 1):
    array[i] = array[i - 1] + array[i - 2]
print(array[n])
end = time.time()
print(end - start)