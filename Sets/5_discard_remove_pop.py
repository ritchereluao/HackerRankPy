# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    c = input().split()
    command = c[0]
    if command == "remove":
        s.remove(int(c[1]))
    elif command == "discard":
        s.discard(int(c[1]))
    elif command == "pop":
        s.pop()
print(sum(s))
