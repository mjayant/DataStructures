def binary_search(sorted_list, item):
    """

    :param sorted_list:
    :return:
    """
    if not sorted_list:
        print("List  is  empty")
        return False
    else :
        midpoint = len(sorted_list)//2
        if item == sorted_list[midpoint]:
            return True
        elif item < sorted_list[midpoint]:
            return binary_search(sorted_list[:midpoint], item)
        else:
            return binary_search(sorted_list[midpoint+1:], item)

