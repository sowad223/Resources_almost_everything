#forward iteration
def Iteration(source):
  for i in range(len(source)):
    print(source[i])
source=[10,20,30,40,50,60]
Iteration(source)

#backword iteration
def reverseIteration(source):
  for i in range(len(source)-1,-1,-1):
    print(source[i])

source=[10,20,30,40,50,60]
reverseIteration(source)
