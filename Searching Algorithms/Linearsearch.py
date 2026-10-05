def linearsearch(a,el):
    ar=[]
    for i in range(len(a)):
        if a[i]==el:
            print(f"{el} is found at index{i}")
            ar.append(i)
    return ar
a=[12,34.56,87,35,87]
print(linearsearch(a,87))