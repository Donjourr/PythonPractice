#There is a number printer from range -100 to 100.
#Input an interval of printing numbers
#Create a tuple that contains the numbers, and print

interval = input('Input the size of interval:')
numbers = []
for i in range(-100, 101, int(interval)):
    numbers.append(i)

print('List of numbers between -100 and 100 that has', interval, 'of interval: ', numbers)