class ArrayStack:

  def __init__(self):
    self.stack = [None]*1000
    self.size = 0

  def push(self, elem):
    flag = self.isfull()
    if flag == False:
      print('Stack Overflow')
    else:
      self.stack[self.size] = elem
      self.size += 1

  def peek(self):
    flag = self.isempty()
    if flag == False:
      print('Stack is empty')
    else:
      return self.stack[self.size-1]

  def pop(self):
    flag = self.isempty()
    if flag == False:
      print('Stack is empty')
    else:
      var = self.stack[self.size - 1]
      self.stack[self.size - 1] = None
      self.size -= 1
      return var

  def isempty(self):
    if self.size < 1: 
      return False 
    else:
      return True

  def isfull(self):
    
    if self.size == len(self.stack):
      return False
    else:
      return True

class Node:
  def __init__(self, elem, next):
    self.element = elem
    self.next = next

class LinkListStack:
  def __init__(self):
    self.head = None
    
  def print(self):
    n = self.head
    while n != None:
      print(n.element, end = ',')
      n = n.next
    print()

  def push(self, elem):

      n1 = Node(elem, None)
      n1.next = self.head
      self.head = n1
      
  def peek(self):
    if self.head == None:
      print('Stack Underflow')
    else:
      top = self.head.element
      return top

  def pop(self):
    if self.head == None:
      print('Stack Underflow')
    else:
      var = self.head.element
      self.head= self.head.next
      return var

  def isempty(self):
    if self.head == None:
      return False
    else:
      return True

class toBalance:

  def __init__(self,bracket,idx,string1):

    self.bracket = bracket
    self.index = idx

    flag = True
    idx = 0

    for i in string1:
      idx += 1
      if i == '(' or i == '{' or i == '[':
        self.bracket.push(i)
        self.index.push(idx)

      elif i == ')' or i == '}' or i == ']':
        
        emp_flag = self.bracket.isempty()

        if emp_flag == False:
          print(f"This expression is NOT correct. \nError at character #{idx}. '{i}' - not opened.")
          flag = False
          break

        else:

          lst_elem = self.bracket.peek()
          if lst_elem == '(' and i == ')':
            self.bracket.pop()
            self.index.pop()

          elif lst_elem == '{' and i == '}':
            self.bracket.pop()
            self.index.pop()

          elif lst_elem == '[' and i == ']':
            self.bracket.pop()
            self.index.pop()

          else:
            idx = self.index.pop()
            
            print(f"This expression is NOT correct. \nError at character #{idx}. '{lst_elem}' - not closed.") 
            flag = False
            break

    if flag == False:
      pass
    else:
      var = self.bracket.isempty()
      if var == True:
        flag = False
        print('This expression is NOT correct.')
      if flag == True:
        print('This expression is correct.')

string11 = "1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
string12="1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"


print("USING ARRAY BASED STACK: ")
bracket = ArrayStack()
idx2 = ArrayStack()
array = toBalance(bracket,idx2,string11)
array = toBalance(bracket,idx2,string12)
print()
print("USING LINKED LIST BASED STACK: ")
bracketLink = LinkListStack()
idxLink = LinkListStack()
linkedlist = toBalance(bracket,idx2,string11)
linkedlist = toBalance(bracket,idx2,string12)
