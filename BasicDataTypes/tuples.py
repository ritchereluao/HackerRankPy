# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    stdout = [num for num in integer_list]
    tuple_stdout = tuple(stdout)
    print(hash(tuple_stdout))
    
