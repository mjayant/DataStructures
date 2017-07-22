def bubbleSort(coll):
    """

    :param self:
    :param coll:
    :return:
    """

    for i in range(len(coll)-1):
        for k in range(0, len(coll)-1):

            try:
                if coll[k] > coll[k + 1]:
                    coll[k+1] ,coll[k] = coll[k], coll[k+1]
            except:
                print("K value-------->"+str(k))
                print(k)
                print(coll)
                print("exception block is ended")

    print("******************************Sorted List***************************")
    print(coll)
    print("==========================Function is ended here ===========================")


def bubbleSortSecondWay(slist):
    """

    :param slist:
    :return:
    """
    print("*************we are inside bubbleSortSecondWay*******************")

    for i in range(len(slist)-1, 0, -1):
        for k in range(i):
            if slist[k] > slist[k+1]:
                slist[k], slist[k+1] = slist[k+1], slist[k]


alist = [54,26,93,17,77,31,44,55,20]
bubbleSortSecondWay(alist)
print(alist)