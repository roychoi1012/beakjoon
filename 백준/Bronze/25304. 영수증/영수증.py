# 영수증 _ SINGO

X = int(input())

N = int(input())

val = 0

for i in range(N):
    a, b = map(int, input().split())
    val += a * b

if val == X:
    print("Yes")
else:
    print("No")