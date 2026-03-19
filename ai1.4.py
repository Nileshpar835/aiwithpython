# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# fruits = ['apple', 'banana', 'orange', 'strawberry']
#
# mixed_List=[1,"apple",True,"banana"]
#
# print(numbers[2])
# print(fruits[0])
# print(mixed_List[2])
# print(numbers[-2])
#
# numbers.append(100)
# numbers.insert(1,12)
# numbers.remove(12)
#
# del numbers[2]
#
# numbers.pop()
# numbers.pop()
#
#
# print(numbers)

# slicing
# fruits = ['apple', 'banana', 'orange', 'strawberry']
# sliced_fruits = fruits[1:3]
# print(sliced_fruits)

# colors = ('red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'cyan')
#
# single_item=("glass",)
#
# print(colors[0])
# print(colors[-1])
# student={"name":"Nilesh","age":22,"College":"BMIIT"}
# student["Subject"]="IT"
# student["age"]=23
#
# del student["Subject"]
#
# student.pop("College")
#
# print(student)

# for key,value in student.items():
#     print(key,":",value)

# numbers={1,2,3,4,5,6,7,8,9,10}
# empty_set=set()
# print(numbers)
#
# numbers.add(44)
# print(numbers)
#
# numbers.remove(44)
# print(numbers)

# set1={1,2,3,4,5}
# set2= {5, 6, 7, 8, 9}
#
# #union
# print(set1 | set2 )
#
# #intersec
# print(set1 & set2 )
# # ?diffecrnce
# print(set1-set2 )
#

#
# data={"name":"nilesh","age":22,"phone_number":9876543210}
# print(data)
# #add new key data
# data["Address"]="katargam"
# print(data)
#
# data["age"]=25
# print(data)
#
#
# if "phone_number" in data:
#     del data["phone_number"]
#
# print(data)

#word frequency counter-------
# sentance = input("Enter a sentence: ")
#
# #split the sentance into word
#
# words=sentance.split()
# #ini dectionaruy
# word_count={}
#
# #count word freq
# for word in words:
#     word=word.lower()
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
#
# print(word_count)

# mylist=[1,2,3,4,5,6,7,8,9,9,8,9]
# print(mylist)
#
# new_Set=set(mylist)
# print(new_Set)
#
# new_list=list(new_Set)
# print(new_list)
#
# new_list.reverse()
# print(new_list)

