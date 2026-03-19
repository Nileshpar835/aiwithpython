# write a program to count how many palindrome words exixts in a sentence

sentence = input("Enter a Sentence : ")

words = sentence.split()
palindrome=[]

for word in words:
    rev=""
    for ch in word:
        rev = ch +rev
    if word == rev:
        palindrome.append(word)

print("Number of palindrome words", len(palindrome))
print("palindrome words", palindrome)