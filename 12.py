#Write a program to find Fibonacci sequence.
#The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#The next number is found by adding up the two numbers before it:
n = int(input("enter n value="))
#0,1,1,2,3
n1 = 0
n2 = 1
count = 0
if n<=0:
    print("enter a valid number")
elif n==1 :
    print("fibonacci series of 1 is 0")    
else:
    while(count<n):
        print(n1)
        nextelement = n1+n2
        n1 = n2   #swapping
        n2 = nextelement
        count = count + 1
        
        
