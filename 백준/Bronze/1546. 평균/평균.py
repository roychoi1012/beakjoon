N = int(input())

score_list = list(map(int, input().split()))

max_val = max(score_list)
final = 0

for i in score_list:
    change_score = i / max_val * 100
    final += change_score

print(final / N)