# 나머지 _ SINGO

num_list = []

for _ in range(10):
    n = int(input())
    num_list.append(n % 42)

num_set = set(num_list)

print(len(num_set))