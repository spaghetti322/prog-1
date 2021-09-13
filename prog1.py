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
    i = 0
    while(i < (len(unsorted_list))):
        if unsorted_list[i] == 0:
            unsorted_list.remove(0)
        i += 1
    return unsorted_list


def make_dict(some_list):
    d = dict.fromkeys(['str', 'num'])


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return np.sqrt((self.x)**2+(self.y)**2)

    def __str__(self):
        return f"x coordinate: {self.x}\ny coordinate: {self.y}\nnorm: {self.norm()}"

    def __lt__(self, other):
        return

l = [1, 2, 0, 3, 0, 5, 6, 7]
vector = Vector2D(1, 2)
print(str(vector))
'''print(is_even(4))
print(generate_squares(1, 5))
print(split_list(l))'''
