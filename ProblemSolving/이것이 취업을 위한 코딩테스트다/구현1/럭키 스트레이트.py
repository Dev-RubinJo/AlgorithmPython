# 백준 18406

n = input()
front = []
end = []

pivot = len(n) // 2

for i in range(pivot):
    front.append(int(n[i]))
for i in range(pivot, len(n)):
    end.append(int(n[i]))

if sum(front) == sum(end):
    print("LUCKY")
else:
    print("READY")