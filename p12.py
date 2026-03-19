# program to count the frequency of each characcter in the input string and display the result banana b=1 a=3 n=2

string = input("Enter a string : ")

freq = {}
for ch in string:
    if ch in freq:
     freq[ch] +=1
    else:
       freq[ch] = 1

for key,value in freq.items():
   print(key,"=",value)
