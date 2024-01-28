#---------------------------
#Title: soto_calculator.py
#Author: Victor Soto
#Date: 01/28/2024
#Sources:
#      https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3
#      https://www.programiz.com/python-programming/examples/calculator
#---------------------------

# Define the functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def multiply(x, y):
    return x * y

# Variables to test each function
add1, add2 = 4, 4
sub1, sub2 = 10, 6
div1, div2 = 8, 2
mul1, mul2 = 10, 2

# Use an output variable to build a string for the results
output = str(add1) + " + " + str(add2) + " is " + str(add(add1, add2)) + ".\n"
output += str(sub1) + " - " + str(sub2) + " is " + str(subtract(sub1, sub2)) + ".\n"
output += str(div1) + " / " + str(div2) + " is " + str(divide(div1, div2)) + ".\n"
output += str(mul1) + " * " + str(mul2) + " is " + str(multiply(mul1, mul2)) + "."

# Print the output variable
print(output)