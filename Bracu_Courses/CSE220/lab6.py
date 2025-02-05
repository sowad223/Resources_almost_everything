#1.a Implement a recursive algorithm to find factorial of n.   
def factorial(n):
  if n==1:
    return n
  else:
    return n*factorial(n-1)
print(factorial(3))

#1.b Implement a recursive algorithm to find the n-th Fibonacci number.

def fibonaccci(n):
  if n<=0:
    return None
  elif n==1 or n==2:
    return 1
  else:
    return fibonaccci(n-1)+fibonaccci(n-2)
n=5
print(fibonaccci(n))

#1.c Print all the elements of a given array recursively.
def print_array(arr,n):
  if n==0:
    return 
  else:
    print_array(arr,n-1)
    print(arr[n-1])
arr=[1,2,3,4]
n=len(arr)
print_array(arr,n)

#1.d Given base and n that are both 1 or more, compute recursively (no loops) 
# the value of base  to the n power, so powerN(3, 2) is 9 (3 squarewwd). 

def Power_N(n,p):
  if p==0:
    return 1
  else:
    return n*Power_N(n,p-1)
n=3
p=6
print(Power_N(n,p))


# 2a) decimal number n  to its corresponding binary number.

def binary(decimal):

  if decimal >1:
    binary(decimal//2)
  print(decimal%2, end="")

binary(15)
# 2 b) Implement a recursive algorithm to add all the elements of a non-dummy headed singly linked linear list. Only head of the list will be given as parameter where you may assume every node can contain only integer as its element.
# Note: you’ll need a Singly Node class for this code.
class Node:
  def __init__(self,e,n):
    self.element=e
    self.next=n
class Linkedlist:
  def __init__(self,a):
    if type(a)==list:
      head=Node(a[0],None)
      self.head=head
      temp=head
      for i in range(1,len(a)):
        n1=Node(a[i],None)
        temp.next=n1
        temp=n1
    else:
        self.head=a
def add(lin_list):
  if lin_list == None:
    return 0
  else:
    return lin_list.element+add(lin_list.next)

lst=[10, 20, 30, 40]
lin_list=Linkedlist(lst)
test_1=add(lin_list.head)
print(test_1)

# 2 c) Implement a recursive algorithm which will print all the elements of a non-dummy headed singly linked linear list in reversed order.
class Node:
  def __init__(self,e,n):
    self.element=e
    self.next=n
class Linkedlist:
  def __init__(self,a):
    if type(a)==list:
      head=Node(a[0],None)
      self.head=head
      temp=head
      for i in range(1,len(a)):
        n1=Node(a[i],None)
        temp.next=n1
        temp=n1
    else:
        self.head=a
  
def rev_print(lin_list):
  if lin_list==None:
    return 
  else:
    rev_print(lin_list.next)
    print(lin_list.element) 

lst=[10, 20, 30, 40]
lin_list=Linkedlist(lst)
test2=rev_print(lin_list.head)

#3
def hoc_buid(n):
  if n==0:
    return 0
  elif n==1:
    return 8
  return 5+ hoc_buid(n-1)

print(hoc_buid(5))


#4.a
def column(n):
  if n==0:
      return 
  else:
      column(n-1)
      print(n,end=' ')

def row(n):
    if n==0:
        return
    else:
        row(n-1)
        column(n)
        print()
row(5)

#4.b
def rev_pattern(m,n):
  if m==0:
    return
  empty_space(m-1)
  pattern(n-m+1,1)
  print()
  rev_pattern(m-1,n)

def empty_space(a):
  if a==0:
    return
  print(" ",end ="")
  empty_space(a-1)

def pattern(m,n):
    if m==0:
        return
    print(n,end="")
    pattern(m-1,n+1)
m=5
rev_pattern(m,m)

#5
class FinalQ:
    def print(self,lst,idx):
        if (idx<len(lst)):
            profit=self.calcProfit(lst[idx])
            print(f"{idx+1}. Investment: {lst[idx]}; Profit: {self.calcProfit(lst[idx])} ")
            return self.print(lst,idx+1)

    def calcProfit(self,investment):
        if investment<=25000:
            return 0.0
        elif investment>25000 and investment<=100000:
            return 45+self.calcProfit(investment-1000)
        elif investment>100000:
            return 80+self.calcProfit(investment-1000)
        else:
            return 0

array=[25000,100000,250000,350000]
f=FinalQ()
f.print(array,0)
