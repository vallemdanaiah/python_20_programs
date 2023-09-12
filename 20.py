#determine the largest and the smallest element of an array which is not sorted.
#method-1
'''numbers = [12,10,9,44,88]
#smallest:9,largest:88
print(min(numbers),max(numbers))'''


#method-2
numbers = [12,10,9,44,88]
numbers.sort()
print(numbers[0],numbers[-1])
