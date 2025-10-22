# 공 바꾸기 _ SINGO

N, M = map(int, input().split())

num_list = [i for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())   
    val = num_list[i] 
    num_list[i] = num_list[j]
    num_list[j] = val

print(*num_list[1:])