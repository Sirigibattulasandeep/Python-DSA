class Stack:
  def __init__(self,size):
    self._a=[]
    self._top=None
    self.size=size
  def push(self,data):
    if self._top is not None:
        if self._top+1==self.size:
          print('stack overflow')
          return
    if self._top is None:
      ar=[]
      ar.append(data)
      self._a=ar
      self._top=0
    else:
      ar=[]
      for i in self._a:
        ar.append(i)  
      ar.append(data)
      self._a=ar
      self._top+=1
  def peek(self):
    if self._top is None:
      return "No element"
    return self._a[self._top]
  def append(self,data):
      if self._top is None:
        self._a.append(data)
        self._top=0
      else:
        self._a.append(data)
        self._top+=1
  def pop(self):
      if self._top is None:
          return "Stack Underflow"
      ar=[None for i in range(self._top)]
      for i in range(self._top):
          ar[i]=self._a[i]
      temp=self._a[-1]
      self._top-=1
      self._a=ar
      if self._top==-1:
        self._top=None
      return temp
stack=Stack(3)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
# print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())