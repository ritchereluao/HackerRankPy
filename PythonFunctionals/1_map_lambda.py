# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x**3 # complete the lambda function     

def fibonacci(n):
    # return a list of fibonacci numbers
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
    l = []
    for i in range(n):
        if i == 0 or i == 1:
            l.append(i)
        else:
            s = l[-1] + l[-2]
            l.append(s)
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
