#sum of the all numbers
n=int(input('enter any number='))
sum=0
for i in range(1,n+1):
    sum=sum+i  
print('sum of the first {} natural numbers is ={}'.format(n,sum))
