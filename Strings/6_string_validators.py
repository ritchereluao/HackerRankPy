# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    
    print(any(each_char.isalnum() for each_char in s))
    print(any(each_char.isalpha() for each_char in s))
    print(any(each_char.isdigit() for each_char in s))
    print(any(each_char.islower() for each_char in s))
    print(any(each_char.isupper() for each_char in s))
