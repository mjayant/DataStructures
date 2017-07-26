def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        print("List is --------->" + str(x))
        print("x[i]---->" + str(x[i]))
        first_part = quicksort(x[:i])

        print("first part------->"+str(first_part))
        second_part = quicksort(x[i + 1:])
        print("x[i]---->" + str(x[i]))
        print("second part--------->"+str(second_part))
        print("We are appending first part---> %s with x[i]---->%s" %(str(first_part), str(x[i])))
        first_part.append(x[i])
        return first_part + second_part


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quicksort(alist)
print(alist)

