#Calculate the number of vowels and consonants in a string .
#vowels==[a,e,i,o,u]
#ex-1 danaiah--vowels=4  consonants:3

name = input("enter any name=")
vowelslist = ['a','e','i','o','u']
vowelscount = 0
consonantscount = 0
for i in name:
    if (i in vowelslist):
        vowelscount = vowelscount+1
    else:
        consonantscount = consonantscount+1
print("number of vowels:{}, number of consonants:{}".format(vowelscount,consonantscount))

        
        
