# 빠른 A+B _ SINGO

import sys

T = int(input())

for i in range(T):
    input_list = sys.stdin.readline().rstrip().split()
    int_list = list(map(int, input_list))
    print(sum(int_list))
