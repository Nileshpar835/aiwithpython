# read interger and calculate the sum of integer 

num = int(input("Enter DIgit "))
total = 0

while num>0:
    digit = num % 10
    total +=digit
    num = num//10

print("Sum of Digits", total)
