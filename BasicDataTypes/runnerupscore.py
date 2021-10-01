# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    l = []
    m = list(arr)
    for nums in m:
        if nums not in l:
            l.append(nums)
    print(sorted(l)[-2])
