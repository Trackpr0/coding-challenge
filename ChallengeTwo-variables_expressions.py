#Challange Two - Variables and expressions
#name is a variable while what is assigned is Alice (sting)
name = "Alice"
#String uses quotes. Typically '' for smaller and "" for longer statements 
age = 25
# the interpreter can determine the data type of each variable based on what is assigned to it.
print(f"Hello, {name}! You are {age} years old.")
''' 
Here you can see we utilized our assigned variables to display a message with their values. 
Lets say though for instance you want to know what type the value is.
'''
print('type for name:', type(name))
print('type for age:', type(age))

'''
You can also review and object's identity using id()
'''
print('id for name:', id(name))
print('id for age:', id(age))

'''
finding out the type also helps determine the mutability of the objects value it was assigned. 
'''