#In r mode we can read the content of file by using read() function.
'''with open("prctice.txt",'r') as f:
    print(f.read())'''

'''with open("abc123.txt",'r') as f:
    print(f.readlines())'''
# read adata in th form of list without \n in last of every line we use splitlines()function.

'''with open("abc123.txt",'r')as f:
    print(f.read().splitlines())'''

# w-mode
# in w mode the we can rewritw the file if the previous dsts is present in the file 
'''f=open("prctice.txt",'w')
for i in range(3):
    n=input("enter the string:")
    f.write(n)
    f.write("\n")
f.close
print("data saved....")'''


# In a-mode the position of pointer is at the end of the previosly written data  and the new data is added just after the previous data.no previous data is deleted.
with open("prctice.txt",'a') as f:
    for i in range(2):
        n=input("enter the string:")
        f.write(n)
        f.write("\n")
print("data saved....")

# r+ is the mode in file handling  is the read and write mode in which the pointer is positioned in begining  of the data and previous data will not be deleted.
'''with open("prctice.txt",'r+') as f:
    n= input("enter the string: ")
    f.write(n)
print("data processed........")'''

# W+ mode in file handling is the write and read mode in which previous data will be deleted.
'''with open("prctice.txt",'w+') as f:
    n= input()
    f.write(n)
print("Data processed.....")'''

# a+ mode in file handling is the append and read mode  in which previous data will not be deleted and new data will be added to the end of the previous data.
'''with open("prctice.txt",'+a') as f:
    str=input("enter the string: ")
    f.write("\n")
    f.write(str)
print("data processed.....")'''
 
# PRACTICE PROGRAMS....

'''with open("abc123.txt",'w') as f:
    while str!='@':
        str= input("enter the data")
        if str!='@':
            f.write(str+'\n')
print("data processd....")'''

# to check the prescence of file in the system entered by the user.
# we first hvae to import the os sys libraray.
'''import os,sys
f_name=input("Enter the filename: ")
#now we will check the library of os by using os.path\\
if os.path.isfile(f_name):
    f=open(f_name,'r')

else:
    print("file does not exist")
    sys.exit()
print(f.read())
f.close'''

#  to enter the data continuosly in the file and finally print it at once.
#  here first we have to append the data first.
#  htis makes pointer move at the end.
#  from where we have to take that pointer at the starting.
#  for this we use seek() function.
# in seek() two parameter are taken.
# seek(offset,fromwhere)
# offset-----> how many bytes to be moved.
# fromwhere----> positon---0----> represent from begning
#                       ---1-----> represents from current positon
#                       ---2--> represent from last
'''f= open("abc123.txt",'a+') 
print("enter the data to be append:")
while str != '@':
    str= input() 
    if str !='@':
        f.write(str +'\n')
f.seek(0,0)
print(f.read())'''

# there is one more funciton tell().
# current position of cursor.
#print(f. tell())

'''with open("prctice.txt",'r') as f:
    print(f.tell())
    print(f.read(15))
    print(f.tell())'''