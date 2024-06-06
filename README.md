#Python print() function prints the message to the screen or any other standard output device
Example
# Python Program to print Hello World 
print("Hello World! I Don't Give a Bug") 
# output
Hello World! I Don't Give a Bug
#Python input () function first takes the input from the user and converts it into a string.
#Example
name = input('What is your name?\n')    
print(name)
#output
What is your name?
Ram
# Data Types in python
1.Strings
2.Numbers
3.Booleans
4.Python List
5.Python Tuples
6.Python Sets
7.Python Dictionary
8.Python Arrays
#example
Integer: 10
Float: 20.5
Complex: (3+4j)
String: Hello, World!
Boolean True: True
Boolean False: False
List: [1, 2, 3, 4, 5]
Tuple: (1, 2, 3, 4, 5)
Set: {1, 2, 3, 4, 5}
Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
NoneType: None
# Expression and operators in python
In Python, expressions are combinations of values, variables, and operators that evaluate to a value. Operators are special symbols or keywords that are used to perform operations on values and variables.
1. Arithmetic Operators
   #example
a = 10
b = 3

print("Addition:", a + b)           # Output: 13
print("Subtraction:", a - b)        # Output: 7
print("Multiplication:", a * b)     # Output: 30
print("Division:", a / b)           # Output: 3.3333333333333335
print("Modulus:", a % b)            # Output: 1
print("Exponentiation:", a ** b)    # Output: 1000
print("Floor Division:", a // b)    # Output: 3
2. Comparison Operators
# Example
print("Equal:", a == b)             # Output: False
print("Not Equal:", a != b)         # Output: True
print("Greater Than:", a > b)       # Output: True
print("Less Than:", a < b)          # Output: False
print("Greater Than or Equal:", a >= b)  # Output: True
print("Less Than or Equal:", a <= b)     # Output: False
3. Logicl Operators
#example
x = True
y = False

print("Logical AND:", x and y)      # Output: False
print("Logical OR:", x or y)        # Output: True
print("Logical NOT:", not x)        # Output: False
4. Bitwise Operators
#Example
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print("Bitwise AND:", a & b)        # Output: 0 (0000 in binary)
print("Bitwise OR:", a | b)         # Output: 14 (1110 in binary)
print("Bitwise XOR:", a ^ b)        # Output: 14 (1110 in binary)
print("Bitwise NOT:", ~a)           # Output: -11 (inverts all bits)
print("Left Shift:", a << 1)        # Output: 20 (10100 in binary)
print("Right Shift:", a >> 1)       # Output: 5 (0101 in binary)
5. Assignment Operators
#example
a = 5
print("Initial a:", a)              # Output: 5
a += 2
print("Add and Assign:", a)         # Output: 7
a -= 2
print("Subtract and Assign:", a)    # Output: 5
a *= 2
print("Multiply and Assign:", a)    # Output: 10
a /= 2
print("Divide and Assign:", a)      # Output: 5.0
a %= 3
print("Modulus and Assign:", a)     # Output: 2.0
a **= 2
print("Exponent and Assign:", a)    # Output: 4.0
a //= 3
print("Floor Divide and Assign:", a)# Output: 1.0

6. Identity Operators
 #example
a = [1, 2, 3]
b = a
c = a[:]

print("a is b:", a is b)            # Output: True
print("a is not c:", a is not c)    # Output: True
print("a == c:", a == c)            # Output: True (They have the same content)
print("a is c:", a is c)            # Output: False (Different objects in memory)
 
7. Membership Operators
   #example
   a = [1, 2, 3, 4, 5]

print("3 in list:", 3 in a)         # Output: True
print("6 not in list:", 6 not in a) # Output: True



#conditional statements
1. if :
   #example
   x = 10

if x > 5:
    print("x is greater than 5")             #output: x is greater than 5
2.elif: 
a < b:
    print(f"{a} is less than {b}")
3.else:
    print(f"{a} is equal to {b}")


# Looping Statements
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1




# Jumping Statements
# break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)
#Some Special functions in python
 len() function returns the number of items in an object 

 id() function returns the unique identifier  of an object.

 type() function returns the type of an object 

 range() function generates a sequence of numbers within a specified range and is commonly used in for loops.

 
