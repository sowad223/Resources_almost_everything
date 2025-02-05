# Test 01: Shift Left k cell
def shift_left(source, k):
  # TO DO
  for j in range(k):
    for i in range(0,len(source)-1):
      source[i]=source[i+1]
    source[len(source)-1]=0
  return source
source = [10,20,30,40,50,60]
print(shift_left(source, 3))








# Test 02: Rotate Left k cell
def rotate_left(source, k):
  # TO DO
  for j in range(k):
    temp=source[0]
    for i in range(1,len(source)):
      source[i-1]=source[i]
    source[len(source)-1]=temp
  return source
source = [10,20,30,40,50,60]
print(rotate_left(source, 3))




# Test 03: Shift Right k cell
def shift_right(source, k):
  # TO DO
  for j in range(k):
    for i in range(len(source)-1,0,-1):
      source[i]=source[i-1]
    source[0]=0
  return source
source = [10,20,30,40,50,60]
print(shift_right(source, 3))








# Test 04: Rotate Right k cell
def rotate_right(source, k):
  # TO DO
  for j in range(k):
    temp=source[len(source)-1]
    for i in range(len(source)-1,0,-1):
      source[i]=source[i-1]
    source[0]=temp
  return source
source = [10,20,30,40,50,60]
print(rotate_right(source, 3))








# Test 05: Remove an element from an array
def remove(source, idx):
  # TO DO
  for i in range(idx,len(source)-1):
    source[i]=source[i+1]


  return source
source = [10,20,30,40,50,0,0]
print(remove(source, 2))








# Test 06: Remove all occurrences of a particular element from an array
def remove_all(source, element):
  new=[0]*len(source)
  j=0
  for i in range(len(source)):
    if source[i]!=element:
      new[j]=source[i]
      j=j+1


  return new
source = [10,2,30,2,50,2,2,0,0]
print(remove_all(source, 2))






# Test 07: Splitting an Array
def split_array(a):
  f_half=0
  l_half=0
  flag=False
  for i in range(0,len(a)):
    for j in range(len(a)-1,0,-1):
      f_half=f_half+a[i]
      l_half=l_half+a[j]
      if f_half==l_half:
        flag=True
        break
        
  return flag


test_1 = [1, 1, 1, 2, 1] 
split_array(test_1)
test_2 = [2, 1, 1, 2, 1]
split_array(test_2)
test_3 = [10, 3, 1, 2, 10] 
print(split_array(test_3))


# Test 08: Max Bunch Count
def max_bunch(a):
  # TO DO
  count=1
  max_count=1
  for i in range(1,len(a)):
    if a[i]==a[i-1]:
       count=count+1
    else:
      count=1
    if count>max_count:
      max_count=count
  return max_count


print(max_bunch([1, 2, 2, 3, 4, 4, 4]))
print(max_bunch([1, 1, 2, 2, 1, 1, 1, 1]))




#Lab1 Part 2
def result(source):
  a=len(source)
  summ=0
  for i in source:
   summ=summ+i
  mean1=summ/a


  sum1=0
  for i in source:
    sum1=sum1+(i-mean1)**2
  Standard_Deviation=(sum1/(a-1))**0.5
  print(f"The mean of the numbers is: {mean1}\nThe standard deviation is: {Standard_Deviation:.2f}")
  first=mean1-1.5*Standard_Deviation
  second=mean1+1.5*Standard_Deviation
  count=0
  for i in range(len(source)):
     if source[i]<first or source[i]>second:
      count=count+1
      arr=[0]*count
      j=0
      arr[j]=source[i]
      j=j+1
      if j>len(arr):
          break
      
   


  return arr 
source=[10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
print(result(source))




 
