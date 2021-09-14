# Simon Leary

import random
from timeit import Timer

def test_counting_sort():
    global alist
    global largest
    global sorted1 # this is for testing purposes, delete this line
    sorted1 = counting_sort(alist, largest)

def counting_sort(alist, largest):
    # copied from https://gist.github.com/mikezink/9fc56a20cebc9076a4f180de3c60b094
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    # Find the last index for each element
    # c[0] = c[0] - 1  # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort
    # for x in reversed(alist):
    for j in range(len(alist) - 1, -1, -1):
        result[c[alist[j]] - 1] = alist[j]
        c[alist[j]] = c[alist[j]] - 1
    return result

def test_my_counting_sort():
    global alist
    global largest
    global sorted2 # this is for testing purposes, delete this line
    sorted2 = my_counting_sort(alist, largest)

def my_counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    result = [0] * (len(alist))
    nextUnfilledIndex = 0 # this is incremented as the empty result is filled outqw
    # index i of c is the number of elements from alist with the value i
    # however many that is, add that many elements with the value i to the result
    for i in range(len(c)):
        value = i
        quantity = c[i]
        for j in range(quantity):
            result[nextUnfilledIndex] = value
            nextUnfilledIndex += 1
    return result

if __name__ == "__main__":
    while True:
        print('generating a new dataset...')
        alist = [random.randint(0, 99) for _ in range(1000000)]
        largest = max(alist)
        # these will be redefined to the return value of the two algorithms
        sorted1 = []
        sorted2 = []
        print('sorting the same 1000000 element list of integers from 0 to 99:')
        timer = Timer('test_counting_sort()', setup="from __main__ import test_counting_sort",globals=globals())
        print("   counting_sort:",timer.timeit(number=1))
        timer2 = Timer('test_my_counting_sort()', setup="from __main__ import test_my_counting_sort",globals=globals())
        print("my_counting_sort:",timer2.timeit(number=1))
        if sorted1 == sorted2:
            print("the two sorted arrays are equal!")
        else:
            print("the two sorted arrays are different. Something went wrong...")
        input("press enter to run again, ctrl+c to quit (ctrl + f2 in PyCharm)")