#Search a missing number in an array that contains integers from 1 to 100.

numbers=[1,2,4,5,6,7,8,9,10]
n = len(numbers)+1
totalsum = n*(n+1)//2
print("total sum is",totalsum)

sum = 0
for i in numbers:
    sum = sum+i
print("missing number is:",totalsum-sum)
