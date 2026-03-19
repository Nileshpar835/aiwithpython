# count vowels and constonants in a string

String = (input("Enter String :- "))
StringL = String.lower()


Vowels ={'a','e','i','o','u'}
Vowels_count=0
Constonants_count=0

for char in StringL:
    if char.isalpha():
        if char in Vowels:
            Vowels_count += 1
        else:
            Constonants_count += 1

print("Vowels" ,Vowels_count)
print("Consonants",Constonants_count)
