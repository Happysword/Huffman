import math


def heapify_up(array, index=-1):
    if index == -1:
        index = len(array) - 1
    parent_index = math.floor((index-1)/2)
    if parent_index < 0 or array[index].frequency > array[parent_index].frequency:
        return
    else:
        array[index], array[parent_index] = array[parent_index], array[index]
        heapify_up(array, parent_index)


def pop_heap(array):
    array[0], array[len(array)-1] = array[len(array)-1], array[0]
    x = array.pop()
    heapify_down(array)
    return x


def heapify_down(array, index=0):
    last_element_index = len(array) - 1
    child_index = index*2 + 1
    if last_element_index == index or index*2 + 1 > last_element_index:
        return
    if child_index+1 < last_element_index and array[child_index].frequency > array[child_index+1].frequency:
        child_index += 1

    if array[child_index].frequency < array[index].frequency:
        array[child_index], array[index] = array[index], array[child_index]
        heapify_down(array, child_index)

    return


def traverse_heap(root, dictionary, code=''):
    if root is None:
        return
    if root.character is not None:
        dictionary[root.character] = code
        return

    traverse_heap(root.left, dictionary, code + '0')
    traverse_heap(root.right, dictionary,code + '1')
    return


class Node:
    character: chr
    frequency: int
    left: None
    right: None

    def __init__(self, c, f):
        self.character = c
        self.frequency = f


#test = "aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff"


def saad_please_i_need_the_codes(test):

    my_list = []

    my_dictionary = {}

    for i in test:
        if i in my_dictionary:
            my_dictionary[i] += 1
        else:
            my_dictionary[i] = 1

    for i in my_dictionary:
        my_list.append(Node(i, my_dictionary[i]))
        heapify_up(my_list)

    while len(my_list) > 1:
        x = pop_heap(my_list)
        y = pop_heap(my_list)
        z = Node(None, x.frequency + y.frequency)
        z.left = x
        z.right = y
        my_list.append(z)
        heapify_up(my_list)

    for i in my_dictionary:
        my_dictionary[i] = ''

    traverse_heap(my_list[0], my_dictionary)
    root = my_list[0]
    
    return (my_dictionary,root)

