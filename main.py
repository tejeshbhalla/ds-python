class Node():
  def __init__(self,data):
    self.data=data
    self.next=None


class Stack():
  def __init__(self):
    self.count=0
    self.head=None
    self.tail=None

  def push(self,data):
    if self.count==0: # first_element
      new_node=Node(data) #new node initialized
      self.head=new_node
      self.tail=new_node
      self.count+=1

    else:
      new_node=Node(data)
      new_node.next=self.head
      self.head=new_node
      self.count+=1

  def pop(self):
    if self.count==0:
      return -1
    data=self.head.data
    self.head=self.head.next
    self.count-=1
    return data

  def size(self):
    return self.count

  def top(self):
    if self.count==0:
      return -1,'empty stack'
    data=self.head.data
    return data    


  def is_empty(self):
    return self.count==0

  def print_stack(self):
    str_=''
    curr=self.head
    while curr!=None:
      str_+=str(curr.data)+';'
      curr=curr.next
    return f'The stack elements are -{str_}'
      

s1=Stack()
for i in range(10):
  s1.push(i)
  print(s1.print_stack())
  s1.pop()