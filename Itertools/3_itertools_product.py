# https://www.hackerrank.com/challenges/compress-the-string/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

stdout = list(product(a, b))
print(*stdout)
