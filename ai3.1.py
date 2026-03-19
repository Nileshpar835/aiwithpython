# # vector and matrix
# # addition & substraction
#
import numpy as np
#
#
# # A=np.array([[1,2],[3,4]])
# # B=np.array([[5,6],[7,8]])
#
# # print("addition :-\n", A+B)
# # print("subtraction :-\n", B-A)
#
# # C=2*A
# # print("Scalar Multiplication :-\n", C)
#
# # matrix multiplication
#
# # result=np.dot(A,B)
# # print("Matrix multiplication result=\n",result)
#
# # special matrix
# # I=np.eye(5)
# # print("Identity matrix \n",I)
#
# # zero matrix
# Z=np.zeros((3,3))
# print("Zeros\n",Z)
#
# # diagonal matrix
# D=np.diag([1,2,3])
# print("dialonal matrix \n",D)
#
#
# # exercise
# # create matrixces
# # A=np.array([[1,2],[3,4]])
# # B=np.array([[9,8],[7,6]])
# # print("Adition :-\n",A+B)
# # print("sub :\n",A-B)
#
# # matrix vector multi
# M=np.array([[1,2,3],[4,5,6],[7,8,9]])
# V=np.array([1,0,-1])
#
# # matrix vector multiplication
# result=np.dot(M,V)
# # print("m vector multiolication\n",result)
#
# # special matrixces
#
# # identity matrix
# I=np.eye(3)
# A=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.dot(A,I))
#
# # diagonal and zeromatrix
#

Two=np.array([[1,2],[4,5]])


det=np.linalg.det(Two)
inv=np.linalg.inv(Two)



print("det\n",det)

print("inv\n",inv)

print("muulti\n",det*inv)

print("muulti\n",inv*det)


