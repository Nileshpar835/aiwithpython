# reverse the string without using reverse function

string = input("ENter a String : ")

reversed_string = ""

for ch in string:
    reversed_string = ch + reversed_string

print("Reversed string :", reversed_string)