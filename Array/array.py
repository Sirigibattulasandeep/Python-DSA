def traverse(array):
  print('[',end="")
  for i in range(len(array)-1):
    print(array[i],end=", ")
  print(array[-1],end="]")


def insert(array,element,index):
    arr2=[0 for i in range (len(array)+1)]
    for i in range (index):
        arr2[i]=array[i]
    for i in range (index,len(array)):
        arr2[i+1]=array[i]
    arr2[index]=element
    print(arr2)   
    

def deletion(array,index):
    if index<=0 or index>=len(array):
        print("invalid size")
    else:
        arr=[0 for i in range(len(array)-1)]
        for i in range (index):
            arr[i]=array[i]
        for i in range (index+1,len(array)):
            arr[i-1]=array[i]
    print(arr)

def search(array,element):
    for i in range(len(array)):
        if a[i]==element:
            print(f"element {element} is  found at index {i}")
    else:
        print(f"element {element} is not found")
a=[1,2,3,4,5]
print(a)
traverse(a)
print()
insert(a,10,3)
print()
deletion(a,3)
print()
search(a,12)