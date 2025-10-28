# 바구니 뒤집기 _ SINGO

N, M = map(int, input().split())

num_list = [i for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    sub_list = num_list[i:j+1]
    reversed_list = sub_list[::-1]
    
    num_list[i:j+1] = reversed_list

print(*num_list[1:])