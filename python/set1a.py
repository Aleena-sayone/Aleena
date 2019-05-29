n = input("enter value of n:")
if(n.isdigit()):    
    dict1={}
    for i in range(1,int(n)+1):    
        dict1.update({i:i*i})
    print("output :", dict1)
else:
    print("please enter a number..!")