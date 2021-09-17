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
    #some_dict = dict.fromkeys(['str', 'num'])
    l_num = []
    l_str = []
    l_str_counter = 0
    l_num_counter = 0
    for i in range(len(some_list)):
        if isinstance(some_list[i], int) or isinstance(some_list[i], float):
            l_num.append(some_list[i])
            l_num_counter += 1
        if isinstance(some_list[i], str):
            l_str.append(some_list[i])
            l_str.append(len(some_list[i]))
            l_str_counter += 2
    some_dict = {'str': l_str, 'num': l_num}
    return some_dict


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return np.sqrt((self.x)**2+(self.y)**2)

    def __str__(self):
        return f"x coordinate: {self.x}\ny coordinate: {self.y}\nnorm: {self.norm()}"

    def __lt__(self, other):
        return (Vector2D.norm(self)) < (Vector2D.norm(other))

    def __le__(self, other):
        return (Vector2D.norm(self)) <= (Vector2D.norm(other))

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return self is not other

    def __gt__(self, other):
        return (Vector2D.norm(self)) > (Vector2D.norm(other))

    def __ge__(self, other):
        return (Vector2D.norm(self)) >= (Vector2D.norm(other))


l = [1, 2, 'sda', 3., 0, '123h', 6, 7]
vector=Vector2D(4,5.5)
vector1=Vector2D(4,5.5)
vector2=Vector2D(1,1)

print(vector.norm())
print(vector1.norm())
print(vector>vector2)