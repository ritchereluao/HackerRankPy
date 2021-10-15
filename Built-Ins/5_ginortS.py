# https://www.hackerrank.com/challenges/ginorts/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

stdin = input()

uppers = []
lowers = []
evens = []
odds = []

for char in stdin:
   if char.isalpha():
        if char.isupper():
            uppers.append(char)
        else:
            lowers.append(char)
   else:
        if int(char)%2 == 0:
            evens.append(char)
        else:
            odds.append(char)
 
        
stdout = sorted(lowers) + sorted(uppers) + sorted(odds) + sorted(evens)
# print(stdout)
print("".join(stdout))
