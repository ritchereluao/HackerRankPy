# https://www.hackerrank.com/challenges/piling-up/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    
    i = 0
    while i < len(cubes) - 1 and cubes[i] >= cubes[i+1]:
        i += 1
    while i < len(cubes) - 1 and cubes[i] <= cubes[i+1]:
        i += 1

    if i == len(cubes) - 1:
        print("Yes")
    else:
        print("No")
