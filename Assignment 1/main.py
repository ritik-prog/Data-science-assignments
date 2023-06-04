# Q1. Create one variable containing following type of data:
a = "ritik"

# Q2. Given are some following variables containing data:
var1 = "" # String
var2 = "[ DS , ML , Python ]" # String 
var3 = [ "DS" , "ML" , "Python" ] # List
var4 = 1 # Number/Int

# Q3. Explain the use of the following operators using an example:
# (i) / -> division
# (ii) % -> modulo
# (iii) // -> floor/integer division 
# (iv) ** -> exponentiation operator 

# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
#     element and its data type.
my_list = [10, 3.14, "Hello", True, [1, 2, 3], {"name": "John", "age": 25}, (4, 5, 6), None, 1000, 1 + 2j]

for element in my_list:
    print(element, type(element))

# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
#     times it can be divisible.
A = 42
B = 7
count = 0

while A % B == 0:
    A = A // B
    count += 1

print("A is divisible by B {count} times.")

# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
#     divisible by 3 or not.
my_list = range(25)

for element in my_list:
    if element % 3 == 0:
        print(f"{element} is divisible by 3")
    else:
        print(f"{element} is not divisible by 3")

# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
#     this property.

# -> The fundamental difference between mutable and immutable data types is that 
#    mutable objects can be modified in-place, while immutable objects cannot be
#    modified once they are created.

# Immutable data type (str)
name = "Alice"
print("Before modification:", name)

name = "Bob"
print("After modification:", name)

# mutable data type (list)
toys = ["car", "ball", "teddy bear"]
print("Before modification:", toys)

toys.append("train")
print("After modification:", toys)

