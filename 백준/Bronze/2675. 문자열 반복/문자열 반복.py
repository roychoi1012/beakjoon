# 문자열 반복 _ SINGO

T = int(input())
word = ''

for _ in range(T):
    R, S = input().split()
    for i in range(len(S)):
        word += S[i] * int(R)
    print(word)
    word = ''