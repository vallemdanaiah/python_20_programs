#Write a program to check whether two strings are anagrams.
'''
An anagram of a string is another string that contains same characters, only the order of characters can be different.
For example, “abcd” and “dabc” are anagram of each other.'''
name1 = input("enter name-1=")
name2 = input("enter name-2=")

if (len(name1)==len(name2)):
    if(sorted(name1)==sorted(name2)):
        print("these are anagrams")
    else:
        print("these are not anagrams")
else:
    print("these are not anagrams")
