a=input("Top Board: ")
b=input("Bottom Board: ")
if len(a)>10 or len(b)>10:
  print("Invalid Input Size")
else:
      arr=[[""]*10,[""]*10]
      aidx=0
      acap=0
      for i in range(len(a)):
        arr[0][i]=a[i]
        if arr[0][i]>="A" and arr[0][i]<="Z":
            aidx=i
            acap=a[i]
      bidx=0
      bcap=0
      for j in range(len(b)):
        arr[1][j]=b[j]
        if arr[1][j]>="A" and arr[1][j]<="Z":
          bidx=j
          bcap=b[j]
      print(f"Top Board Start Character, {acap} and  its index {aidx}")
      print(f"Bottom Board Start Character, {bcap} and its index {bidx}")

def circular_left_shift(arr1,k):
    word1=""
    n = len(arr1)
    rotated_arr = [0]*len(arr1)
    temp=arr1[0]
    for i in range(0,len(arr1)-1):
        rotated_arr[i]=arr1[i+1]
    rotated_arr[len(arr1)-1]=temp
    for i in rotated_arr:
      word1=word1+i

    return word1

def circular_Right_shift(arr2,k):
    word2=""
    n = len(arr2)
    rotated_arr2 = [0]*len(arr2)
    temp2=arr2[len(arr2)-1]
    for i in range(len(arr2)-1,-1,-1):
        rotated_arr2[i]=arr2[i-1]
    rotated_arr2[0]=temp2
    for i in rotated_arr2:
      word2=word2+i

    return word2
while True: 
  user_input=input("Press Any key to continue and q to stop: ")
  if user_input!="q":
    newarray=arr[0] 
    newarray=circular_left_shift(arr[0] ,1)
    print(newarray)
    arr[0]=newarray
    newarray2=arr[1]
    newarray2=circular_Right_shift(arr[1] ,1)
    print(newarray2)
    arr[1]=newarray2
    
  else:
    break
  
          
