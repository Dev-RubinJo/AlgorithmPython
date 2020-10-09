while True:
    n = input()
    if n == '0':
        break
    length = int(len(n) / 2)
    isPalindrom = True
    for i in range(length):
        if n[i] != n[len(n) - (i + 1)]:
            isPalindrom = False
            break
    print("yes" if isPalindrom else "no")