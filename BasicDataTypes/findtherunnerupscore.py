# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    listed_arr = list(arr)
    l = []
    for each_number in listed_arr:
        if each_number not in l:
            l.append(each_number)
    print(sorted(l)[-2])
    
