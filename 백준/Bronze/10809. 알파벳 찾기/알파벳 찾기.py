# 알파벳 찾기 _ SINGO

alp_list = [-1] * 26

S = input()
for i in range(len(S)):
    alp_list[ord(S[i]) - 97] = S.index(S[i])
print(*alp_list)

