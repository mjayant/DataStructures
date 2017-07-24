def merge(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def mergeSort(alist):
    """

    :param alist:
    :return:
    """
    if len(alist) == 0 or len(alist) == 1:
        return alist
    else:
        mid = int(len(alist)/2)
        print(alist)
        a = mergeSort(alist[:mid])
        b = mergeSort(alist[mid:])
        print("list a -------->" +str(a))
        print('list b ------>'+ str(b))
        c = merge(a, b)
        print("list c---------" + str(c))
        return c




    # if len(x) == 0 or len(x) == 1:
    #     return x
    # else:
    #     middle = int(len(x)/2)
    #     a = mergeSort(x[:middle])
    #     b = mergeSort(x[middle:])
    #     return merge(a,b)





print (mergeSort([54,26,93,17,77,31,44,55,20]))

# Code for the merge subroutine

# def merge(a,b):
#     """ Function to merge two arrays """
#     c = []
#     while len(a) != 0 and len(b) != 0:
#         if a[0] < b[0]:
#             c.append(a[0])
#             a.remove(a[0])
#         else:
#             c.append(b[0])
#             b.remove(b[0])
#     if len(a) == 0:
#         c += b
#     else:
#         c += a
#     return c
#
# # Code for merge sort
#
# def mergesort(x):
#     """ Function to sort an array using merge sort algorithm """
#     if len(x) == 0 or len(x) == 1:
#         return x
#     else:
#         middle = int(len(x)/2)
#         a = mergesort(x[:middle])
#         b = mergesort(x[middle:])
#         return merge(a,b)
#
# print (mergesort([54,26,93,17,77,31,44,55,20]))