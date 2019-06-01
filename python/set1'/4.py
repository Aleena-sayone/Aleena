str1=input("enter your input here   :")
list1=str1.split(",")
list2=[]
f=0
for i in sorted(list1):
    if(i.isdigit()):        
        f=1
        break 
    else:
        list2.append(i)            

if(f!=0):
    print("Numbers not allowed..!")
else:
    print("sorted list  :",list2)    
    print(', '.join(list2))
       






