def copyArray(source):
  new_array=[0]*len(source)
  for i in range(len(source)):
    new_array[i]=source[i]
  return new_array
source=[10,20,30,40,50,60]
copyArray(source)

def resizeArray(oldArray, newCapacity):
  new_array=[0]*newCapacity
  for i in range(newCapacity):
    new_array[i]=oldArray[i]
  return new_array


oldArray=[10, 20, 30, 40, 50, 60]
resizeArray(oldArray, 4)
