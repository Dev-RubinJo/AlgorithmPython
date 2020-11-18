encrypt = input()

dp = [0 for _ in range(len(encrypt) + 1)]
dp[0], dp[1] = 1, 1

if encrypt[0] == "0":
    print(0)
else:
    for i in range(2, len(encrypt) + 1): # dp[1]까지는 만들었으니 2부터 돌림
        if int(encrypt[i - 1]) > 0: # 일단 첫번째 숫자는 뭐가 됐든 문자가 한개다. 그래서 2부터 돌리면서 0보다 큰지 체크
            dp[i] += dp[i - 1] # 0보다 크다면 이전까지의 암호문 수를 더해준다.
        number = int(encrypt[i - 1]) + int(encrypt[i - 2]) * 10 # 두자리 수로 만들어준다
        if number >= 10 and number <= 26: # 두자리 수가 10 ~ 26사이라면
            dp[i] += dp[i - 2] # 이전전꺼도 포함시킨다.
    print(dp[len(encrypt)] % 1000000)