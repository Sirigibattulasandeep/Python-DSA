#1st problem
def sumofArray(a): 
  sum=0
  for i in a:
    sum=sum+i
  return sum
n=int(input())
a=[]
for i in range(n):
  ele=int(input())
  a.append(ele)
sum=0
for i in a:
  sum=sum+i
print(sum)
res=sumofArray(a)
print(res)
#2nd problem
def search(a,el):
  c=0
  for i in a:
    if el==i:
      c=c+1
  return c
n=int(input())
a=list(map(int,input().split(' ')))
ele=int(input())
#search(a,ele)
print(search(a,ele))
#3rd problem
n=int(input())
a=list(map(int,input().split(' ')))
sumvalue=0
for i in a:
  sumvalue+=i
res=sumvalue/n
print(res)
print(f'{res:.2f}')
#4th problem
def remove(string):
  for ch in string:                                                                  
    if  ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
      string=string.replace(ch,"")
  return string
string=input()
result=remove(string)
print(result)

def traversal(a):
  print('[',end="")
  for i in range(len(a)-1):
    print(a[i],end=", ")
  print(f'{a[-1]}]')
a=[1,2,3,4,5]
print(a)
traversal(a)
#insertion of array
def insert(ar,el,ind):
  ar2=[0 for i in range(len(a)+1)]
  for i in range(ind):
    ar2[i]=ar[i]
  for i in range(ind,len(ar)):
    ar2[i+1]=a[i]
  ar2[ind]=el
  return ar2  
n=int(input())
a=list(map(int, input().split(' ')))[:n]
print(a)
el=int(input())
ind=int(input())
a=insert(a,el,ind)
print(a)
#deletion of array
def delete(ar,el):
  ar2=[0 for i in range(len(a)-1)]
  for i in range(el):
    ar2[i]=ar[i]
  for i in range(el,len(ar)-1):
    ar2[i]=a[i+1]
  return ar2  
n=int(input())
a=list(map(int, input().split(' ')))[:n]
print(a)
el=int(input())
a=delete(a,el)
print(a)
#right rotation
def rotaion(a,key):
  ar=[0 for i in range(len(a))]
  ind=0
  for i in range(len(a)-key,len(a)):
    ar[ind]=a[i]
    ind+=1
  for i in range(len(a)-key):
    ar[ind]=a[i]
    ind+=1  
  return ar 
n=int(input())
a=list(map(int, input().split(' ')))[:n]
print(a)
ind=int(input())
a=rotaion(a,ind)
print(a)
#left rotation
def rotation(a,key):
  ar=[0 for i in range(len(a))]
  ind=0
  for i in range(key,len(a)):
    ar[ind]=a[i]
    ind+=1
  for i in range(key):
    ar[ind]=a[i]
    ind+=1
  return ar
n=int(input())
a=list(map(int, input().split(' ')))[:n]
print(a)
ind=int(input())
a=rotation(a,ind)
print(a)
#sliding window
def maxsubarray(a,k):
  sum=0;
  for i in range(k):
    sum+=a[i]
  max=sum
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    if sum>max:
      max=sum
  print(max)
a=[1,2,3,4,5,6,7,1]
print(a)
maxsubarray(a,3)
#linear search
def linearsearch(a,ele):
  ar=[]
  for i in range(len(a)):
    if a[i]==ele:
      ar.append(i)
  return ar    
a=[12,33,2,4,11,10,33,33]
ele=33
print(linearsearch(a,ele))
#remove duplicates
def remove_duplicates(arr):
  ind=1
  ar=[1]
  for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]:
      ar.append(arr[i])
      ind+=1
  return ar
n=[1,2,2,2,3,3,3,4,5]
res=remove_duplicates(n)
print(res)
#container with water
def max_water_container(heights):
  left = 0
  right = len(heights) - 1
  max_water = 0
  while left < right:
      width = right - left
      height = min(heights[left], heights[right])
      water = width * height
      max_water = max(max_water, water)
      if heights[left] < heights[right]:
          left += 1
      else:
          right -= 1
  return max_water
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water_container(heights))
#sum of sub array
def max_sum_subarray(arr, k):
  window_sum = sum(arr[:k])
  max_sum = window_sum
  for i in range(k, len(arr)):
      window_sum = window_sum - arr[i - k] + arr[i]
      max_sum = max(max_sum, window_sum)
  return max_sum
temperatures = [2, 1, 5, 1, 3, 2, 8, 1, 3]
print(max_sum_subarray(temperatures, 3))
#smallest max_sum_subarray
def min_subarray_with_sum(arr, target):
  min_length = float('inf')
  window_sum = 0
  start = 0
  for end in range(len(arr)):
    window_sum += arr[end]
    while window_sum >= target:
        min_length = min(min_length, end - start + 1)
        window_sum -= arr[start]
        start +=1
  return min_length if min_length != float('inf') else 0
numbers = [2, 3, 1, 2, 4, 3]
print(min_subarray_with_sum(numbers, 7))
#prefix array
def prefixarray(a):
  ar=[0 for _ in range(len(a))]
  s=0
  for i in range(len((a))):
    s+=a[i]
    ar[i]=s
  return ar  
a=[3, 1, 4, 1, 5, 9, 2, 6]
print(prefixarray(a))
#Range sum
def range_sum(a,st,end):
  return a[end]-a[st-1]

a=[3, 1, 4, 1, 5, 9, 2, 6]
prefix=prefixarray(a)
print(prefix)
print(range_sum(prefix,2,5))
#subb=array sum equals to target
def sumarray(a,k,target):
  s=0
  if k<=0 or k>len(a):
    return 'invalid key elements'
  for  i in range(k):
    s+=a[i]
  if s==target:
    return [a[i] for i in range(k)]
  for i in range(k,len(a)):
    s=s+a[i]-a[i-k]
    if s==target:
      return [a[i] for i in range(i-k+1,i+1)]
  return -1    
print(sumarray(a,3,10))