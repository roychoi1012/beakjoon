# 공 넣기 _ SINGO

N, M = map(int, input().split())

num_list = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        num_list[x - 1] = k
print(*num_list)
        
