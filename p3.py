#  srite program that reads two string , check whether the string is substring of string1 , do not use inbuild function like substr 

string1= input("enter string 1 ")
string2= input("enter string 2 ")
lel1=len(string1)
len2=len(string2)

found =False

for i in range( lel1 - len2 +1):
    match=True
    for j in range(len2):
        if string1[i+j] != string2[j]:
            match=False
            break
        if match:
            found=True
            break
if found:
  print("strinf 2 is substrin of string 1")
else:
    print("String 2 is not a substring of string 1")
