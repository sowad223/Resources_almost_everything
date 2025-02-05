class keyIndex:
    def __init__(self, a):
        k_len = 0
        self.k = [0]
        self.pos = 0
        minn = a[0]
        maxx = a[0]
        for i in range(1, len(a)):
            if maxx < a[i]:
                maxx = a[i]
            elif minn > a[i]:
                minn = a[i]
        
        self.pos = abs(minn)
        k_len = maxx + self.pos + 1
        self.k = [0] * k_len
        
        for i in a:
            self.k[i+ self.pos] += 1
    
    def search(self, element):
        if element < self.pos*(-1) or element > (len(self.k)-1):
            return False
        else:
            return self.k[element + self.pos] != 0
    
    def sort(self):
        idx = 0
        for i in range(len(self.k)):
            for j in range(self.k[i]):
                a[idx] = i - self.pos
                idx += 1
        return a
a= [-1,-2,3,0,4,-3,3]
Test_1= keyIndex(a)
print(Test_1.search(-1000))
print(Test_1.sort())


# Task 2 on Hashing

hashArray = [None]*9

def hashing(arr):

  vowels = "aeiouAEIOU"
  sum_digit = 0
  t_con = 0
  digits = '0123456789'

  for i in arr:
  
    if i not in vowels and i not in digits:
      t_con +=1

    elif i in digits:
      sum_digit = sum_digit + int(i)
      
  idx1 = (t_con*24 + sum_digit) %9
  return idx1

def linear_probe(arr):

  for i in arr:

    idx = hashing(i) 

    if hashArray[idx] == None:
      hashArray[idx] = i

    else:

      idx = (idx+1)%9
      while hashArray[idx] !=None:
        idx = (idx+1)%9
      hashArray[idx] = i

arr = ["ST1E89B8A32", "YERBB53R", "ZBTRDS","BT34ZRS", "ZT54BRSD","TBZRTRS", "NDT9SRYR", "PAA25DDE"]
test1 = linear_probe(arr)
print(hashArray)
