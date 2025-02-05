#Implement the enqueue, dequeue and peek functions using an array.
class Queue:
  def __init__(self,cap):
    self.queue=[None]*cap
    self.font=0
    self.rear=0
    self.size=0
  def enqueue(self,elem):
    if self.size==len(self.queue):
      return "queue overflow"
    else:
      self.queue[self.rear]=elem
      self.rear=(self.rear+1)%len(self.queue)
      self.size=self.size+1
      return self.queue
  def dequeue(self):
    if self.size==0:
      return "queue Underflow"
    else:
      self.queue[self.font]=None
      self.font=(self.font+1)%len(self.queue)
      self.size=self.size-1
      return self.queue
  def peek(self):
    if self.size==0:
      return "queue Underflow"
    else:
      return self.queue[self.font]




a=Queue(8)
print(a.enqueue(4))
print(a.enqueue(1))
print(a.enqueue(2))
print(a.enqueue(7))
print(a.dequeue())
print(a.enqueue(9))
print(a.enqueue(4))
print(a.enqueue(2))


#Implement the enqueue, dequeue and peek functions using an Linkedlist


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0

  def is_empty(self):
    return self.size == 0

  def enqueue(self, elem):
    new_node = Node(elem)
    if self.rear is None:
      self.front = new_node
      self.rear = new_node
    else:
      self.rear.next = new_node
      self.rear = new_node
    self.size += 1

  def dequeue(self):
    if self.front is None:
      return "queue underflow"
    else:
      dequeued_node = self.front
      self.front = dequeued_node.next
      if self.front is None:
        self.rear = None
      self.size -= 1
      return dequeued_node.data

  def peek(self):
    if self.front is None:
      return "queue underflow"
    else:
      return self.front.data

a = Queue()
a.enqueue(4)
a.enqueue(1)
a.enqueue(2)
a.enqueue(7)
print(a.dequeue())
a.enqueue(9)
a.enqueue(4)
a.enqueue(2)
print(a.peek())
  
