class DoublyList:
  
  def __init__(self, a):
  # Creates a Non Dummy Headed Circular Doubly Linked List using the values from the given array a.
    # To Do
    if type(a) == list:
      self.head = Node(a[0], None, None)
      temp = self.head
      for i in range(1, len(a)):
        n = Node(a[i], None, None)
        temp.next = n
        n.prev = temp
        temp = temp.next
    else:
      self.head = a
    
  
  # Counts the number of Nodes in the list and return the number
  def countNode(self):
    # To Do
    temp = self.head
    count = 0
    while temp is not None:
      count += 1
      temp = temp.next
    return count
  
  # prints the elements in the list
  def forwardprint(self):
    # To Do
    temp = self.head
    while temp is not None:
      if temp.next is not None:
        print(temp.element, end=', ')
        temp = temp.next
      else:
        print(temp.element)
        temp = temp.next

  # prints the elements in the list backward
  def backwardprint(self):
    # To Do
    temp = self.head
    while temp.next is not None:
      temp = temp.next
    while temp is not None:
      if temp.prev is not None:
        print(temp.element, end=', ')
        temp = temp.prev
      else:
        print(temp.element)
        temp = temp.prev

  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    # To Do
    if idx >= self.countNode() or idx < 0:
      n = Node('index error', None, None)
      return n
    else:
      temp = self.head
      count = 0
      while count != idx:
        count += 1
        temp = temp.next
      return temp
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    # To Do
    temp = self.head
    count = 0
    while temp is not None:
      if temp.element is not  elem:
        temp = temp.next
        count += 1
      else:
        return count
    return -1
  # inserts containing the given element at the given index Check validity of index. 
  def insert(self, elem, idx):
    # To Do
     if idx == 0:
      temp = self.head
      self.head = Node(elem, temp, None)
      temp.prev = self.head
     elif idx < self.countNode():
       temp = self.head
       count = 0
       while temp is not None:
         if count + 1 == idx:
           tail = temp.next
           temp.next = Node(elem, tail, temp)
           tail.prev = temp.next
           break
         else:
           count += 1
           temp = temp.next
     elif idx == self.countNode():
       temp = self.head
       count = 0
       while temp is not None:
         if count + 1 == idx:
           tail = temp.next
           temp.next = Node(elem, tail, temp)
           break
         else:
           count += 1
           temp = temp.next
     elif idx > self.countNode() or idx < 0:
       print('index out of range')
  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
  def remove(self, idx):
    # To Do
    if idx == 0:
      temp = self.head
      self.head = temp.next
      self.head.prev = None
      return str(temp.element)
    elif idx == (self.countNode() - 1):
      temp = self.head
      count = 0
      while temp is not None:
        if count == idx:
          tail = temp.prev
          tail.next = None
          return str(temp.element)
        else:
          count += 1
          temp = temp.next
    elif idx < self.countNode():
      temp = self.head
      count = 0
      while temp is not None:
        if count == idx:
          tail = temp.prev
          tail.next = temp.next
          temp.next.prev = tail
          return str(temp.element)
        else:
          count += 1
          temp = temp.next

print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,80.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.
