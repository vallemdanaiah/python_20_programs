n = input('enter any name=')
print('this is original string value',n)
print('this is reverse string value',n[::-1])
if n==n[::-1]:
   
    
    
    print('{} this is palindrome'.format(n))
else:
    print('{} this is not palindrome'.format(n))
    
