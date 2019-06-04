str1=input("enter input :")
list2=[]
if((str1=="") | (str1==",")):
    print("nobody likes this")
elif("," not in str1):
    print(str1, "likes this")
else:
    list1 = str1.split(',')
    for i in list1:
        list2.append(i)
    print(list2)
    if(len(list2)==2):
        print(list2[0]+" and "+list2[1]+" likes this ")
    elif(len(list2)==3):
        print(list2[0] +" , "+list2[1]+" and "+list2[2]+" likes this ")

    else:
        nos = len(list2) -2
        print(list2[0] +","+list2[1]+" and "+ str(nos)+" others likes this ")
