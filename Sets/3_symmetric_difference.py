# https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

stdout = a.symmetric_difference(b)
for each_num in sorted(stdout):
    print(each_num)
