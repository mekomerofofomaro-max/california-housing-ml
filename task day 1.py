#1.
#name = "Amir"  
#age = 18    
#favorite_number = 10.0
#print(f"My name is {name}, I am {age} years old, and my favorite number is {favorite_number}.")
#2.
#a = 7
#b = 2
#print(f"a + b = {a + b}")      
#print(f"a - b = {a - b}")      
#print(f"a * b = {a * b}")      
#print(f"a / b = {a / b}")      
#print(f"a ** b = {a ** b}")
#3.   
#my_int = 42          
#my_float = 3.14      
#my_string = "Python" 
#print(f"The type of my_int is: {type(my_int)}")
#print(f"The type of my_float is: {type(my_float)}")
#print(f"The type of my_string is: {type(my_string)}")  
#4.
#name = input("What is your name? ")
#print(f"Hello, {name}! Welcome to Python.")
#5.
#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#sum_result = num1 + num2
#print(f"The sum of {num1} and {num2} is: {sum_result}")
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#because when remove int the variable change to string and python not add string with intger
#6.
#number = float(input("Enter a number: "))
#if number > 0:
#    print("The number is positive")
#elif number < 0:
#    print("The number is negative")
#else:
#    print("The number is zero")
#7.
#age = int(input("Enter your age: "))
#if age < 18:
#    print("You are a minor")
#elif age < 65:
#    print("You are an adult")
#else:
#    print("You are a senior")
#8.
#num1 = int(input("Number 1: "))
#num2 = int(input("Number 2: "))
#operation = input("Operation: ")
#if operation == "add":
#    result = num1 + num2
#    print(f"{num1} + {num2} = {result}")
#elif operation == "multiply":
#    result = num1 * num2
#    print(f"{num1} * {num2} = {result}")
#elif operation == "subtract":
#    result = num1 - num2
#    print(f"{num1} - {num2} = {result}")
#9.
#hourly_wage = float(input("Hourly wage: "))
#hours_worked = float(input("Hours worked: "))
#day_of_week = input("Day of the week: ")
#if day_of_week == "Sunday":
#    daily_wages = hourly_wage * 2 * hours_worked
#else:
#    daily_wages = hourly_wage * hours_worked
#print(f"Daily wages: {daily_wages} euros")
#10.
#score = int(input("Enter your score (0-100): "))
#if score >= 90:
#    grade = "A"
#elif score >= 80:
#    grade = "B"
#elif score >= 70:
#    grade = "C"
#elif score >= 60:
#    grade = "D"
#else:
#    grade = "F"
#print(f"Your grade is: {grade}")
#11.
#students = int(input("How many students on the course? "))
#group_size = int(input("Desired group size? "))
#groups = (students + group_size - 1) // group_size
#print(f"Number of groups formed: {groups}")