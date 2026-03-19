# read string and remove vowels and return removed vowels string

string = input("ENter String : ")
stringl=string.lower()

vowels={'a','e','i','o','u'}

removed_vowels = ""

no_vowels = ""

for char in stringl:
    if char in vowels:
        removed_vowels += char
    else:
        no_vowels += char
print(removed_vowels)
print("Input String :",stringl)
print("Output String :",no_vowels)
