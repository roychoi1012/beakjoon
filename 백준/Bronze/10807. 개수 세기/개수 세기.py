# 개수 세기 _ SINGO

N = int(input())
num_list = input().split()
int_list = list(map(int, num_list))
v = int(input())
print(int_list.count(v))