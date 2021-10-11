# https://www.hackerrank.com/challenges/py-collections-deque/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    c = input().split()
    command = c[0]
    if command == "append":
        d.append(c[1])
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()
    elif command == "appendleft":
        d.appendleft(c[1])

print(*d)
