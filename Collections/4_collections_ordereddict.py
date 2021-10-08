# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()

for _ in range(N):
    list_items = input().split()
    
    price = int(list_items[-1])
    item_name = " ".join(list_items[:-1])
    
    if ordered_dictionary.get(item_name):
        ordered_dictionary[item_name] += price
    else:
        ordered_dictionary[item_name] = price

for k,v in ordered_dictionary.items():
    print(k,v)
