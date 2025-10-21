# X보다 작은 수

N, X = map(int, input().split())

int_list = list(map(int, input().split()))

result_list = [i for i in int_list if i < X]

print(*result_list)

