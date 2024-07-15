# For loop in Python 
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable
# When we have complete information about the data then apply the for loop

#syntax
# for item in iterable(start,end,step_to_skip):

myList=[1,2,3,4,5,6,7]
for item in myList:
    print( item,end=',') #Output 1,2,3,4,5,6,7,



# While Loop
# While loop is used to iterate over a sequence (list, tuple, string) or other iterable
# A while loop repeatedly executes a block of code as long as a condition is true.

#while condition:
    # code to execute

myList = [1, 2, 3, 4, 5, 6, 7]
i = 0
while i < len(myList):
    print(myList[i], end=',')
    i += 1
  # Output 1,2,3,4,5,6,7