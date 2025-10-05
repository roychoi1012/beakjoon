# 주사위 세개 _ SINGO

import collections

num_list = list(map(int, input().split()))

counts = collections.Counter(num_list)

most_val, most_cnt = counts.most_common(1)[0]

if most_cnt == 1:
    print(max(num_list) * 100)
elif most_cnt == 2:
    print(1000 + most_val * 100)
else:
    print(10000 + most_val * 1000)

