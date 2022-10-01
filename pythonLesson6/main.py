# Declare two numbers with any values
# Check if the first number is greater than 50 and check if the second number is less than 100,
# if True print out "Evaluation is True"
# Add an else block that prints "Evaluation is False"
# Declare a string with value "python"
# Check if the first string is equal to "testify" or "python", if True prints out "Yay!!
# The string is a Testify Python".
# Use the logical and to check if the first number is greater than 50 and the second number is less than 100.

print("Check if the first number is greater than 50 and check if the second number is less than 100,")
number1 = 65
number2 = 70

if number1 >50 and number2 <100:

    print("Evaluation is True")

print("Check if the first number is greater than 50 and check if the second number is less than 100")

number1 = 20
number2 = 120

if number1 >50 and number2 <100:
    print("Evaluation is True")
else:
    print("Evaluation is False")

print("Declare a string with value=python")

name1 ="python"
name2 = "testify"

if name1 == "python" or name2 == "testify":
    
    print("OR: name1 =python, name2 = testify")

print("Check if the first string is equal to testify or python, if True prints out Yay!! The string is a Testify Python")
if name1 == "python" or name2  == "testofy":
    print("Yay!! The string is a Testify Python")

print("Use the logical and to check if the first number is greater than 50 and the second number is less than 100")

number1 = 70
number2 = 20

if number1 >50 and number2 < 100:
    print("AND:number1 =50, number2 =100")