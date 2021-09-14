# Simon Leary

import random
from timeit import Timer

def counting_sort():
    # copied from https://gist.github.com/mikezink/9fc56a20cebc9076a4f180de3c60b094
    # alist and largest are defined globally so that both algorithms can use the same set
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    for i in range(1, largest +1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    for j in range(len(alist)-1, -1, -1):
        result[c[alist[j]]-1] = alist[j]
        c[alist[j]] = c[alist[j]] - 1

    return result

def my_counting_sort():
    # alist and largest are defined globally so that both algorithms can use the same set
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
        print('sorting the same 1000000 element list of integers from 0 to 99:')
        timer = Timer('counting_sort()', setup="from __main__ import counting_sort",globals=globals())
        print("   counting_sort:",timer.timeit(number=1))
        timer2 = Timer('counting_sort()', setup="from __main__ import counting_sort",globals=globals())
        print("my_counting_sort:",timer2.timeit(number=1))
        input("press enter to run again, ctrl+c to quit (ctrl + f2 in PyCharm)")
