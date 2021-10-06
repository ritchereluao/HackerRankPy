# https://www.hackerrank.com/challenges/py-set-union/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
first_line = int(input())
second_line = set(map(int, input().split()))
third_line = int(input())
fourth_line = set(map(int, input().split()))

s = second_line.union(fourth_line)
print(len(set(s)))
