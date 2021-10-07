# https://www.hackerrank.com/challenges/maximize-it/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K_M = input().split()
k = int(K_M[0])
m = int(K_M[1])

stdout = []
# for _ in range(k):
#     output = list(map(int, input().split()))
#     stdout.append(max(output[1:]))
# max_output = 0
# for each_num in stdout:
#     max_output += each_num**2
# print(max_output % m)


for _ in range(k):
    row = map(int,input().split()[1:])
    stdout.append(map(lambda x:x**2 % m, row))
print(max(map(lambda x: sum(x) % m, product(*stdout))))
