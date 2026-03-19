# with open("ai1.5.py","r") as file:
#     content=file.read()
#     print(content)
import shutil


# with open("ai1.5.py","w") as file:
#     file.write("Hello World")
#     file.writelines(["nilehs","Ritik"])

# with open("ai1.1.py","")

# try:
#     with open("sample.py", "r") as f:
#         content=f.read()
#         print(content)
#
# except FileNotFoundError:
#     print("File not found")


# def count_wordsandLines(filename):
#     try:
#         with open(filename,"r") as f:
#              lines=f.readlines()
#              line_count=len(lines)
#              word_count=sum(len(line.split()) for line in lines)
#
#              print("Number of lines :",line_count)
#              print("Number of Words :",word_count)
#     except FileNotFoundError:
#         print(f"File{filename} not found")
#
# count_wordsandLines("sample.py")

#
# def write_itemtofile(filename,items):
#     with open(filename,"w") as f:
#         for item in items:
#             f.write(item+"\n")
#
# def read_itemfromfile(filename):
#     try:
#         with open(filename,"r") as f:
#             item=f.readlines()
#             print("items in the file :-")
#             for item in item:
#                 print(item.strip())
#     except FileNotFoundError:
#         print(f"FIle {filename} not found")
#
# items=["apple","banana","orange","kela","strawberry"]
# write_itemtofile("sample.py",items)
# print(read_itemfromfile("sample.py"))

# def copyfromanotherfile(filename,newfilename):
#     shutil.copy(filename,newfilename)
#
#
# copyfromanotherfile("sample.py","newsample.py")


