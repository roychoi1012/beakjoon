# 코딩은 체육과목입니다 _ SINGO

N = int(input())

val = N // 4
remain = N % 4

if remain == 0:
    print('long ' * val + 'int')
else:
    print('long ' * (val + 1) + 'int')

