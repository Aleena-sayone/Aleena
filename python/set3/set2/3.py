import re
input1 = input("enter the basestring    :")
list1=[]
str1=""
for i in input1:
    if(i.isdigit()):
        str1+=i
    else:
        str1=""
    if(len(str1)==10):
        list1.append(str1)
        str1=""
print("Mobile Numbers are: ")
for i in list1:
    if re.match(r"^[789]{1}\d{9}$", i):
        print(i)
    
