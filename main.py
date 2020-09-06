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
    