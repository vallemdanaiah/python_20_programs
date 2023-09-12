#Find the number of occurrences of a particular character in a string .
'''name = input("enter a name:")
character = input("enter a character:")
print(name.count(character)) #this is the default method'''


name = input("enter a name:")
character = input("enter a character:")
count = 0
for i in name:
    if (character==i):
        count = count+1
print("count of '{}' is {}times".format(character,count))
