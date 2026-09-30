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
    cN=self.head
    i=0
    while cN.next is not None:
      if cN.data==data:
        print(f"data is at {i} found")
        return
      i=i+1
      cN=cN.next
      if cN.data==data:
        print(f"data is at {i} found")
        return
    print("data is not found")
  def delete(self,data):
    cN=self.head
    if self.head==None:
      return False
    if cN.data==data:
      self.head=cN.next
      self.size-=1
    while cN.next is not None:
      if cN.next.data==data:
        cN.next=cN.next.next
        self.size-=1
        return True 
      cN=cN.next
    self.traverse()
  def length(self):
    print(self.size)
  def insertatbeg(self,data):
    obj=Node(data)
    obj.next=self.head
    self.head=obj
    self.traverse()
  def deletelast(self):
    cN = self.head
    while cN.next.next is not None:
        cN = cN.next
    cN.next = None
    self.size -= 1
    self.traverse()
  def insertatposition(self,data,position):
    if self.head is None:
      return
    if position<0 and position>self.length():
      print("invalid position")
      return
    if position ==0:
      self.insertatbeg(data)
      return
    if position==self.length():
      self.add(data)
      return
    cn=self.head
    ind=0
    while cn.next.next is not None:
      if ind+1==position:
        break
      cn=cn.next
    obj=Node(data)
    obj.next=cn.next
    cn.next=obj
    self.size+=1
    self.traverse()
  def insertafter(self,data,targetdata):
    if self.head is None:
      return
    cn=self.head
    while cn.next.next is not None:
      if cn.data==data:
        break
      cn=cn.next
    obj=Node(targetdata)
    obj.next=cn.next
    cn.next=obj
    self.size+=1
    self.traverse()
  def deletebyvalue(self,data):
    if self.head is not None:
      return
    if self.head.next is None:
      if self.head.data==data:
        self.head=None
    cn=self.head
    while cn.next is not None:
      if cn.next.data==data:
        cn.next=cn.next.next
      cn=cn.next
    self.size-=1
    self.traverse()
  def delat(self,position):
    if self.head is None:
      return
    if position<0 and position>self.length():
      print("invalid position")
      return
    if position ==0:
      self.head=self.head.next

      return
    if position==self.length():
      self.add(data)
      return
    cn=self.head
    ind=0
    while cn.next.next is not None:
      if ind==position:
        break
      cn=cn.next
    cn.next=cn.next.next
    self.size-=1
    self.traverse()
    
ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(44)
ll.add(7667)
ll.traverse()
ll.search(10)
ll.delete(10)
ll.length()
ll.insertatbeg(90)
ll.deletelast()
ll.insertatposition(100,3)
ll.insertafter(100,200)
ll.deletebyvalue(100)
ll.delat(3)