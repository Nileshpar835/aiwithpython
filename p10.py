# largest and smallest in array  find the largest and smallers in an array

array = [1,2,10,3,4,5,0,6,7,8,9]

largest = array[0]
smallest = array[0]

for i in range(1 , len(array)):
    if array[i]>largest:
        largest = array[i]

    if array[i]<smallest:
        smallest=array[i]

print("Largest element ", largest)
print("Smallest element : ", smallest)

print("Largest:", max(array))
print("Smallest:", min(array))
