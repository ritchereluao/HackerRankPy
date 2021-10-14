# https://www.hackerrank.com/challenges/input/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = list(map(int, input().split()))
equation = input()

if eval(equation) == k:
    print(True)
else: print(False)
