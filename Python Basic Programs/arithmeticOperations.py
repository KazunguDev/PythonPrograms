# Simple Python program to understand the arithmetical operator addition
# Here, we are storing the first input numbers in num1
from operator import mul

num1 = input('Enter first number: ')
# Here, we are storing the second input numbers in num2
num2 = input('Enter second number: ')
# Here, we are declaring a variable sum to store the result
# Here, we are using the arithmetical operator to add the two numbers
sum = float(num1) + float(num2)
# Here, we are printing the sum of the given two numbers

# Simple Python program to understand the arithmetical operator subtraction
# Here, we are storing the first input numbers in num1
num1 = input('Enter first number: ')
# Here, we are storing the second input numbers in num2
num2 = input('Enter second number: ')
# Here, we are declaring a variable min to store the result
# Here, we are using the arithmetical operator to subtract the two numbers
min = float(num1) - float(num2)
# Here, we are printing the subtraction of the given two numbers

# Simple Python program to understand the arithmetical operator muitiplication
# Here, we are storing the first input numbers in num1
num1 = input('Enter first number: ')
# Here, we are storing the second input numbers in num2
num2 = input('Enter second number: ')
# Here, we are declaring a variable mul to store the result
# Here, we are using the arithmetical operator to multiply the two numbers
Mul = float(num1) * float(num2)
# Here, we are printing the multiplication of the given two numbers

# Simple Python program to understand the arithmetical operator division
# Here, we are storing the first input numbers in num1
num1 = input('Enter first number: ')
# Here, we are storing the second input numbers in num2
num2 = input('Enter second number: ')
# Here, we are declaring a variable div to store the result
# Here, we are using the arithmetical operator to divide the two numbers
div = float(num1) - float(num2)
# Here, we are printing the division of the given two numbers

if __name__ == '__main__':
    print('The division of {0} and {1} is {2}'.format(num1, num2, min))
    print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))
    print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
