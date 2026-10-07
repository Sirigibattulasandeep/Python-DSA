def linearsearch(a, el):
    for i in range(len(a)):
        if a[i] == el:
            print(f'{el} is found at {i} index')
            a.append(i)
            return i
    return -1
a = [12,2,44,23,14,65,14]
linearsearch(a, 14)