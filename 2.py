'''n = input('enter any name=')
print('this is the orginal string',n)
print('this is the reverse string',n[::-1])'''


n = input('enter any name=')
reverse = ''
for i in n:
    reverse = i + reverse
print(reverse)






