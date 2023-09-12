#Delete the repeated elements in an integer array .
#method-1

'''numbers = [1,2,3,3,5,8,2]
print(set(numbers))'''

#method-2
numbers = [1,2,3,3,5,8,2]
newnumbers = []

for i in numbers:
    if(i not in newnumbers):
        newnumbers.append(i)
print("after removing the duplicates",newnumbers)
