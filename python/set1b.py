
str1=input("enter comma seporated numbers : ")
list1 = str1.split(",")
list2=[]
f=0
for i in list1:
    if(i.isalpha()):
        print("invalied input...!  please enter numbers only.")
        f+=2
        break
    else:
        list2.append(i)
if(f==0):
    tuple1=tuple(list2)  
    print("list:", list2)
    print("tuple:",tuple1)

