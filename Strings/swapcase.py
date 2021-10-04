# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    string_s = str(s)
    output = []
    for each_letter in string_s:
        if each_letter == each_letter.lower():
            output.append(each_letter.upper())
        elif each_letter == each_letter.upper():
            output.append(each_letter.lower())
        else:
            output.append(each_letter)
    return "".join(output)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
