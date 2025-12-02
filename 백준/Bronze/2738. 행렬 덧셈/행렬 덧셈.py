# 행렬 덧셈 _ SINGO

N, M = map(int, input().split())
A_matrix = []
B_matrix = []
C_matrix = [[0] * M for _ in range(N)]

for i in range(N):
    inlist = list(map(int, input().split()))
    A_matrix.append(inlist)

for i in range(N):
    inlist = list(map(int, input().split()))
    B_matrix.append(inlist)

for i in range(N):
    for j in range(M):
        C_matrix[i][j] = A_matrix[i][j] + B_matrix[i][j]

for i in range(N):
    print(*C_matrix[i])