# https://www.hackerrank.com/challenges/zipped/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = list(map(int, input().split()))

master_list = []
for _ in range(x):
    num = list(map(float, input().split()))
    master_list.append(num)

for each_list in zip(*master_list):
    stdout = sum(each_list) / len(each_list)
    print(stdout)
