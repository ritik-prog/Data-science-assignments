# Q1. How do you comment code in Python? What are the different types of comments?
# This is a single-line comment
"""
This is a multi-line comment.
It can span multiple lines.
"""

# Q2. What are variables in Python? How do you declare and assign values to variables?
# Variables in Python are used to store data values.
# To declare and assign a value to a variable, you can use the assignment operator "=".
my_variable = 10

# Q3. How do you convert one data type to another in Python?
num_str = "10"
num_int = int(num_str)

float_num = 3.14
int_num = int(float_num)  # Convert float to integer

str_num = str(float_num)  # Convert float to string

# Q4. How do you write and execute a Python script from the command line?
# To write and execute a Python script from the command line, follow these steps:
# 1. Create a new Python file with a .py extension, e.g., my_script.py.
# 2. Write your Python code in the file.
# 3. Save the file.
# 4. Open the command line or terminal.
# 5. Navigate to the directory where the Python file is located.
# 6. Run the script using the "python" command followed by the file name.
# Example: python my_script.py

# Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
my_list = [1, 2, 3, 4, 5]
sub_list = my_list[1:3]
print(sub_list)

# Q6. What is a complex number in mathematics, and how is it represented in Python?
# A complex number is a number of the form a + bi, where 'a' and 'b' are real numbers, and 'i' is the imaginary unit (√-1).
# In Python, complex numbers are represented using the "j" suffix to denote the imaginary part.
complex_num = 2 + 3j

# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
age = 25

# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?
price = 9.99
# "price" belongs to the float data type.

# Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?
name = "Ritik Makhija"
print(name)

# Q10. Given the string "Hello, World!", extract the substring "World".
my_string = "Hello, World!"
substring = my_string[7:12]
print(substring) 

# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.
is_student = True
print(is_student)
