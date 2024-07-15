myList=["Nitish kumar",20,46,94]
print(myList) # Output :[Nitish kumar,20,46,94]
print(myList[0]) # Output : Nitish kumar
print(myList[1]) # Output : 20
print(*myList)   #Output : Nitish kumar 20 46 94

# print list with loop
for element in myList:
    print(element) # Output : Nitish kumar 20 46 94

# Changing a Single Element
myList=["Nitish kumar",20,46,94]
myList[2] = 10  # Change the third element to 10
print(myList)  # Output: ["Nitish kumar",20,10,94]


# Changing Multiple Elements

my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [20, 30]  # Change the second and third elements
print(my_list)  # Output: [1, 20, 30, 4, 5]

# Removing Elements by Value

my_list2 = [22,14,16,47,78,16,98]
my_list2.remove(16)
print(my_list2)  # Output: [22,14,47,78,16,98]

#Removing Elements by Index
my_list2 = [22,14,16,47,78,16,98]
my_list2.pop(2)
print(my_list2)  # Output: [22,14,47,78,16,98]

my_list2.pop()
print(my_list2)  # Output: [22,14,47,78,16]

#Removing Multiple Elements
my_list2 = [22,14,16,47,78,16,98]
del my_list2[1:3]
print(my_list2)  # Output: [22,47,78,16,98]

# Removing All Elements
my_list2 = [22,14,16,47,78,16,98]
my_list2.clear()
print(my_list2)  # Output: []

my_list2 = [22,14,16,47,78,16,98]
del my_list2[:]
print(my_list2)  # Output: []

# Removing Elements Based on a Condition
my_list2 = [22,14,16,47,78,16,98]
while 47 in my_list2:
    my_list2.remove(47)
print(my_list2)  # Output: [22,14,16,78,16,98]
