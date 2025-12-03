# 킹, 퀸, 룩, 비숍, 나이트, 폰 _ SINGO

chess = [1, 1, 2, 2, 2, 8]

num = list(map(int, input().split()))

for i in range(len(num)):
    chess[i] = chess[i] - num[i]
print(*chess)