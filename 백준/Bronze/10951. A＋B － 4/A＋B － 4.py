# A + B - 4 _ SINGO

import sys

while True:
    try:
        line = sys.stdin.readline().rstrip()
        if not line:
            break
        a, b = map(int, line.split())
        print(a + b)
    except EOFError:
        break