# 다이얼 _ SINGO
word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
val = 0

for i in word:
    for j in range(len(dial)):
        if i in dial[j]:
            val += (j + 3)
print(val)





