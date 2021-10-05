# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m = input().split()
n = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

counter = 0
for each_number in n:
    if each_number in A:
        counter += 1
    elif each_number in B:
        counter -= 1

print(counter)
