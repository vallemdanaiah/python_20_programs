#Write a program to calculate the number of numerical digits in a string .
'''
name = input("enter a name:")
count = 0
for i in name:
    if i.isdigit():
        print(i)
        count = count+1'''
 #method2   
name = input("enter a name:")
digitlist = ['0','1','2','3','4','5','6','7','8','9']
count = 0
for i in name:
    if i in digitlist:
        count = count+1
        print(i)
print("number of digits in {} is {}".format(name,count))
        
