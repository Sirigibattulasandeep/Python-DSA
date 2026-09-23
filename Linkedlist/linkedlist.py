class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkedlist:
  def __init__(self):
    self.head=None  
    self.size=0
  def add(self,data):
    if self.head==None:
      self.head=Node(data)
      self.size+=1
      return
    cN=self.head
    while cN.next is not None:
      cN=cN.next
    cN.next=Node(data)
    self.size+=1
  def traverse(self):
    if self.head==None:
      print()
      return
    cN=self.head
    while cN.next is not None:
      print(cN.data,end="->")
      cN=cN.next
    print(cN.data,cN.next)
  def search(self,data):
    if self.head==None:
      print('No elements in LL')
      return
    cN=self.head
    ind=0 
    while cN.next is not None:
      if cN.data==data:
        print(f'element {data} found at {ind} index')
        return
      ind+=1
      cN=cN.next
    if cN.data==data:
      print(f'element {data} found at {ind} index')
      return
    print('element not found')
  def delete(self,data):
    if self.head==None:
      return  False
    cN=self.head
    if cN.data==data:
      self.head=cN.next
      return True
    while cN.next is not None:
      if cN.next.data==data:
        cN.next=cN.next.next
        return True
      cN=cN.next 
  def len(self):
    return self.size-1      
  def insertatStart(self,data):
    obj=Node(data)
    obj.next=self.head
    self.head=obj
  def delatlast(self):
    if self.head == None:
      return False
    if self.head.next == None:
      self.head = None
      return True
    cN = self.head
    while cN.next.next is not None:
      cN = cN.next
    cN.next = None
    return True  
ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.traverse()
ll.search(50)
ll.delete(20)
ll.traverse()
print(ll.len())
ll.insertatStart(30)
ll.traverse()
ll.delatlast()
ll.traverse()