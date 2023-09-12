#Write a program to compute the first character of a string that is not repeated.
#method-1
name = input("enter a name=")
for i in name:
    if(name.count(i)==1):
        print("first non repeated character is:",i)
        break

