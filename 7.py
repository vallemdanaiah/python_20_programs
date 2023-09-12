#Program to swap two numbers without using temporary variable.
'''a,b=10,20  #using the muiltyble assignments.
b,a=a,b
print('{} these are original numbers {} these are swaping  numbers'.format((a,b),(b,a)))'''

#second method.
'''a=10
b=20
print('original values',a,b)
t=a  #using the temprary varible
a=b
b=t

print('swaped values',a,b)'''

#third method.

a=10
b=20
print("original numbers",a,b)
a=a+b #30
b=a-b #10
a=a-b #30-10=20
print('after swaping a={},b={}'.format(a,b))


