str1=input("enter your input here   :")
list1=str1.split(",")
list2=[]
tuple1=tuple(list1)
f=0
for i in tuple1:
    if(i.isalpha()):        
        f=1
        break 
    else:
        if (int(i)%2 ==0):
            list2.append(i)                

if(f!=0):
    print("Numbers Only..!")
else:
    tuple2=tuple(list2)
    print("you have entered: ",tuple1)
    print("New tuple is:", tuple2)
    





