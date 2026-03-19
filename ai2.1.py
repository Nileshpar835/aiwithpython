import numpy as np
#
# arr=np.array([1,2,3,4,5])
# print(arr)

# zeros=np.zeros((3,3))
# # print(zeros)
#
# ones=np.ones((2,4))
# # print(ones)
#
# range_array=np.arange(1,10,3)
# # print(range_array)
#
# linspace_array=np.linspace(0,10,3)
# # print(linspace_array)
#
# arr=np.array([1,2,3,4,5,6,7,8,9])
# # reshape=arr.reshape((3,3))
# # print(reshape)
#
# arr=np.array([1,2,3])
# expanded=arr[:,np.newaxis]
# # print(expanded)
#
#
#
#
# a=np.array([1,2,3])
# b=np.array([4,5,6])
#
# # print(a+b)
# # print(a*b)
# # print(a/b)
# # print(b-a)
#
# arr=np.array([4,16,25])
# # print(np.sqrt(arr))
# # print(np.sum(arr))
# # print(np.mean(arr))
# # print(np.max(arr))


# arr=np.array([10,20,30,40,50,60])
# print(arr[2])
# print(arr[-1])
#
# print(arr[1:4])
# print(arr[:3])
# print(arr[3:])

# reshape=arr.reshape(2,3)
# print(reshape)

# a=np.arange(1,6)
# print(a)
# b=np.arange(6,11)
# print(b)
#
# print("add:",a+b)
# print("sub:",a-b)
# print("mul:",a*b)
# print("div:",a/b)

# matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("Original matrix: \n",matrix)
#
# transpose
# transpose=matrix.T
# print("Transposed matrix: \n",transpose)
#
# another_matrix=np.array([[9,8,7],[6,5,4],[3,2,1]])
# print("addition_matrix: \n",another_matrix+matrix)
# print("Multiplication_matrix: \n",another_matrix*matrix)

#create 4x4 matrix and calculate the sum of its rows and columns
ftf=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
print(ftf)

sum_row=np.sum(ftf,axis=0)
print("Sum of row",sum_row)
sum_column=np.sum(ftf,axis=1)
print("Sum of column",sum_column)





