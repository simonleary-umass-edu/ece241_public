def counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    # Find the last index for each element
    # c[0] = c[0] - 1  # to decrement each element for zero-based indexing
    for i in range(1, largest +1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort
    # for x in reversed(alist):
    for j in range(len(alist)-1, -1, -1):
        result[c[alist[j]]-1] = alist[j]
        c[alist[j]] = c[alist[j]] - 1

    return result

def main():
    # alist = input('Enter the list of (nonnegative) numbers: ').split()
    # alist = [int(x) for x in alist]
    alist = [2,5,3,0,2,3,0,3]
    k = max(alist)
    sorted_list = counting_sort(alist, k)
    print('Sorted list: ', end='')
    print(sorted_list)


from timeit import Timer
timer = Timer('main()')
print(timer.timeit())