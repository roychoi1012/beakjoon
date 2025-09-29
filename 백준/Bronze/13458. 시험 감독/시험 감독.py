# 시험 감독 _ SINGO

N = int(input())

A = input().split()

A_int = list(map(int, A))

B, C = map(int, input().split())

result = 0 

for num in A_int:
    result += 1
    
    remaining = num - B

    if remaining <= 0:
        continue
    
    required_subs = remaining // C

    if remaining % C > 0:
        required_subs += 1
        
    result += required_subs

print(result)