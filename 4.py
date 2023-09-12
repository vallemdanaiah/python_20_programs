n = int(input('enter any number='))
if n<0:
    print('invalied number')
elif n==0:
    print('factroal of o is 1')
else:
    d=1
    for i in range(1,n+1):
        d=d*i
    print('factroal of the {}! is {}'.format(n,d))
