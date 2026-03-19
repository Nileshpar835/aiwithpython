import sys

print(sys.argv)
print(sys.version)




import os
# print(os.getcwd())
# os.mkdir('mydir')
# os.rmdir('mydir')





from functools import  reduce
numbers=[1,2,3,4,5]


product=reduce(lambda x,y:x*y,numbers)
# print(product)

evenList=filter(lambda x:x%2==0,numbers)
# print(list(evenList))

squares=map(lambda x:x**2,numbers)
# print(list(squares))
# print(squares)








#expression for item in iterable if condition

#create a list of squares

# squares=[x**2 for x in range(10)]
# print(squares)
#
# # filter even
#
# evens=[x for x in range(100) if x%2!=0]
# print(evens)

#lambda arguments:expression

add = lambda x,y,:x+y
# print(add(1,2))