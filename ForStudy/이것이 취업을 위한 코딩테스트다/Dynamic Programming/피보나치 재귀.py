import time

def fibo(x):
    if x == 1 or x == 2:
        return x
    return fibo(x - 1) + fibo(x - 2)

start = time.time()

print(fibo(38))

end = time.time()
print((end - start))