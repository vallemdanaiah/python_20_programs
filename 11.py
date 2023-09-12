#Program to get the matching characters in a string.
#m1
'''name='danaiah'
print(name.count('a'))#this is predefind method count the character repet

matchingcharacters = []

for i in name:
    if name.count(i)>1:
        matchingcharacters.append(i)
print(matchingcharacters)'''
        


name='danaiah'
print(name.count('a'))#this is predefind method count the character repet

matchingcharacters = set()

for i in name:
    if name.count(i)>1:
        matchingcharacters.add(i)
print(matchingcharacters)
        
