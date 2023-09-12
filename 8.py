#Write a program to reverse a number .
n=int(input("enter any number=")) #example 531
originalval=n
reverse = 0
while(n>0):
    num = n%10
    reverse = reverse*10+num
    n=n//10
print('reverse of number {} is {}'.format(originalval,reverse))
