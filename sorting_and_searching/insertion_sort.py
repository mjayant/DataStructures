def insertion_sort(alist):
    """

    :param alist:
    :return:
    """
    for i in range(len(alist)):
        val = alist[i]
        for k in range(i, -1, -1):
            if val < alist[k]:
                #import pdb ;pdb.set_trace()
                # print('alist[i]------>'+str(alist[i]))
                # print('alist[k]------>' + str(alist[k]))
                alist[k], alist[k+1] = val, alist[k]
                print(alist)

    return alist


alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)