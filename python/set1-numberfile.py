input_file = input("Enter File name : ")
file_txt = open(input_file)		# default it will open in read mode
text = file_txt.read()			# to read file-object    
space=0
line=0
charc = 0		# initialising variables to 0 
    
for i in text:					# reading text character by character
    if(i == " "):
        space += 1
    elif(i == "\n"):
        line += 1
    else:
        charc += 1
    
print (" Spaces = {} \n Lines = {} \n Characters = {}".format(space,line,charc))