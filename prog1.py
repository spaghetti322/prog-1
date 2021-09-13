import numpy as np

def is_even(number):
    if number < 0:
        return 'Error.'
    elif number % 2 == 0:
        return True
    else:
        return False


def generate_squares(min_num, max_num):
    l = []
    for i in range(max_num-min_num+1):
        l.append((min_num+i)**2)
    return l


def split_list(unsorted_list):
    i=0
    while(i<(len(unsorted_list))):
        if unsorted_list[i] == 0:
            unsorted_list.remove(0)
        i+=1
    return unsorted_list


print(is_even(3))
print(generate_squares(1, 5))
l = [1, 2, 0, 3, 0, 5, 6, 7]
print(split_list(l))
