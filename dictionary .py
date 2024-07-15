 # Creating a Dictionary
myDictionary={
    "Name":"Rahul",
    "Age":20,
    "City":"Delhi"
      }
print(myDictionary) # Output {'Name': 'Rahul', 'Age': 20, 'City': 'Delhi'}
print(*myDictionary) # Output Name Age City

# Accessing Values with help of key
print(myDictionary["Name"]) # Output Rahul
print(myDictionary["Age"]) # Output 20

# Adding or Modifying Values
myDictionary['Name']='Nitish'
print(myDictionary) # Output {'Name': 'Nitish', 'Age': 20, 'Delhi'}
myDictionary['Phone_Number']=987654321
print(myDictionary) # Output {'Name': 'Nitish', 'Age': 20, 'City': 'Delhi', 'Phone_Number': 987654321}

# Removing Key-Value Pairs
# 'del' statement
del myDictionary['Phone_Number']
print(myDictionary) # Output {'Name': 'Nitish', 'Age': 20, 'City': 'Delhi'}
# pop() method
myDictionary.pop('Age')
print(myDictionary) # Output {'Name': 'Nitish', 'City': 'Delhi'}
