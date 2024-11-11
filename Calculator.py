# ----------------------------------------
# Author: Shudufhadzo Mulaudzi
# Project: Calculator
# Date Created: 11/11/2024
# Description: This is my first python project, a simple calculator
# GitHub: https://github.com/ShuduMulaudzi
# ----------------------------------------

print("Hello, World!")

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error! Invalid operation"
    return a / b

def calculator():
    print("Select the opertation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter the number of the operation you want to do 1,2,3,4 :")
    
    if operation in ['1','2','3','4']:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        if operation == '1':
             print(f"The reuslt of addition: {number1} + {number2} = {add(number1,number2)}")
        elif operation == '2':
             print(f"The reuslt of subtraction: {number1} - {number2} = {subtract(number1,number2)}")
        elif operation == '3':
             print(f"The reuslt of multiplication: {number1} * {number2} = {multiply(number1,number2)}")
        elif operation == '4':
             print(f"The reuslt of division: {number1} / {number2} = {divide(number1,number2)}")
    else:
        print("Invalid input. Please select a number between 1 and 4.")
        
calculator()
