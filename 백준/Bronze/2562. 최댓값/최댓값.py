# 최댓값 _ SINGO

num_list = []

for i in range(9):
    num = int(input())
    num_list.append(num)

max_val = max(num_list)

print(max_val)
print(num_list.index(max_val)+1)