# 단어 공부 _ SINGO

word = input().upper()
word_dict = {}
word_list = []

for i in word:
    if i not in word_dict:
        word_dict[i] = 1
    else:
        word_dict[i] += 1

max = max(word_dict.values())

for key, value in word_dict.items():
    if value == max:
        word_list.append(key)

if len(word_list) == 1:
    print(*word_list)
else:
    print('?')
