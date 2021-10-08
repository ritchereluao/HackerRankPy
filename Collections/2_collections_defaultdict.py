# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

# group_a = [input() for _ in range(n)]
# group_b = [input() for _ in range(n, n+m)]
# for b in group_b:
#     for i in range(n):
#         if b not in group_a:
#             d[b].append(-1)
#         elif b in group_a:
#             if b == group_a[i]:
#                 d[b].append(i+1)     
# for i in d.values():
#     print(*i)

l = []
for i in range(n):
    d[input()].append(i+1) 

for _ in range(m):
    l.append(input())

for item in l: 
    if item in d:
        print(*d[item])
    else:
        print(-1)
