values = input("enter values  of list  : ")
list1=values.split(",")
list2=[]
f=0
for i in list1:
    if(i.isalpha()):        
        f=1
        break 
    else:
        if (int(i)%2 !=0):
            list2.append(i)           

if(f!=0):
    print("Numbers Only..!")
else:    
    print("Smallest odd number is:", min(list2))