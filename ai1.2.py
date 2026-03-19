# num=10
# if num>0:
#     print("positive number")
# elif num==0:
#     print("zero number")
# else:
#     print("negative number")

# age=32
# if age>18:
#     if age<30:
#         print("young adult")
#     else:
#         print("Adult")
#

#for loop

# fruits=['apple','banana','mango','cherry','pineapple']
# i=1
# for fruit in fruits:
#     print(i,"Fruits is",fruit)
#     i+=1

# for i in range(10):
#     print(i)


# count=5
# while count>0:
#     print(count)
#     count-=1
# print("outside while")
#


# for i in range(10):
#     if i==5:
#          # break
#       continue
#     print(i)
#
# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

# num=int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             print(num,"is not prime")
#             break
#     else:
#             print(num,"is prime")
# else:
#     print(num,"is not prime")

#
# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#       if b!=0:
#           return a/b
#       else:
#           print("Cant divide by zero")
#
# while True:
#     print("\nMenu: ")
#     print("1. Add a number")
#     print("2. Subtract a number")
#     print("3. Multiply a number")
#     print("4. Divide a number")
#     print("5. Quit")
#     choice=int(input("Enter your choice: "))
#     if choice==5:
#         print("Exiting.....")
#         break
#     num1=float(input("Enter the First Number:"))
#     num2=float(input("Enter the Second Number:"))
#
#     if choice==1:
#         print("Result: ",add(num1,num2))
#     elif choice==2:
#         print("Result: ",sub(num1,num2))
#     elif choice == 3:
#         print("Result: ", div(num1, num2))
#     elif choice == 4:
#         print("Result: ", mul(num1, num2))
#     else:
#         print("Enter a valid choice")



# fact=1
# i=1
# while i<=num:
#     fact=fact*i
#     i=i+1
# print(num,":- Factorial is: ",fact)


# list=[1,2,3,4,5,6,7,8,90,10]
# largest=list[0]
#
# for numbers in list:
#     if numbers > largest:
#         largest=numbers
# print("Largest number is:-",largest)










