# 오븐 시계 _ SINGO

# 입력값
A, B = map(int, input().split())
C = int(input())

if B + C < 60:
    print(f'{A} {B + C}')
else:
    hours = A + (B + C) // 60
    if hours < 24:
        print(f'{hours} {(B + C) % 60}')
    else:
        num = hours - 24
        print(f'{num} {(B + C) % 60}')
    





