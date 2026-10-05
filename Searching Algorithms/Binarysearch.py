#Binary Search
def binarysearch(a,el):
  l=0
  r=len(a)
  while l<r:
    m=(l+r)//2
    if a[m]==el:
      return m
    elif l==m:
      return -1
    elif a[m]<el:
      l=m
    else:
      r=m

a=[1,2,3,4,5,6,7,8,9]
print(binarysearch(a,9))