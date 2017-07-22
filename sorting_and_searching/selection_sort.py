def selection_sort(alist):
    """

    :param alist:
    :return:
    """
    for i in range(len(alist)-1, 0, -1):
        maxIndex = 0
        for k in range(i):
            if alist[maxIndex] < alist[k+1]:
                maxIndex = k + 1
        print(maxIndex)
        alist[i], alist[maxIndex] = alist[maxIndex], alist[i]

    return alist


print (selection_sort([54,26,93,17,77,31,44,55,20]))