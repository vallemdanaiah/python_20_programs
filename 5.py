'''#theck the armstrong condation?
n = int(input('enter a number='))
to_str = str(n)
for i in to_str:
    sum = int(i)*int(i)*int(i)#this condation is check the armstrong
    print(sum)'''


#program to check wheater a number is armstrong or not?
'''n = int(input('enter a number='))
to_str = str(n)
sum = 0
for i in to_str:
    sum = sum  + int(i)*int(i)*int(i)#this condation is check the armstrong
if n==sum:
    print('{}is armstrong'.format(n))
else:
    print('not armstrong')
print('program is completed')'''


#this is the another way?
n = int(input('enter a number='))
to_str = str(n)
sum = 0
for i in to_str:
    #sum = sum  + int(i)*int(i)*int(i)#this condation is check the armstrong or
    #sum = sum + pow(int(i),3) or 
    sum = sum + (int(i)**3)
if n==sum:
    print('{}is armstrong'.format(n))
else:
    print('not armstrong')
print('program is completed')
