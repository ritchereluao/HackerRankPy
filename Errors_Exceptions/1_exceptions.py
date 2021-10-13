# https://www.hackerrank.com/challenges/exceptions/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for _ in range(t):
    try:
        values = list(map(str, input().split()))
        a = int(values[0])
        b = int(values[1])
        print(a//b)
    except Exception as e:
        print("Error Code:", e)
