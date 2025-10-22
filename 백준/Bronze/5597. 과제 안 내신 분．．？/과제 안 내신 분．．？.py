# 과제 안 내신 분..? _ SINGO

num_list = list(range(1, 31))

for _ in range(28):
    num_list.remove(int(input()))

num_list.sort()

print(num_list[0])
print(num_list[1])

