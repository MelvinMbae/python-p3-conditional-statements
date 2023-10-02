#!/usr/bin/env python3

def admin_login(username, password):

    if username == "sudo" and password == "12345":
        return "Access denied"
    elif username == "admin" and password == "12345":
        return "Access granted"
    elif username == "ADMIN" and password == "12345":
        return "Access granted"
    else: return "Access denied"
    
print(admin_login("ADMIN", "12345"))

def hows_the_weather(temperature):
   if temperature < 40:
       return "It's brisk out there!"
   elif temperature >= 40 and temperature < 65:
       return "It's a little chilly out there!"
   elif temperature > 85:
       return "It's too dang hot out there!"
   else: return "It's perfect out there!"
   
print(hows_the_weather(89))

def fizzbuzz(num):
    # Define condition for whether num is divisible by both 3 and 5. Use and operator
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    
    # Define condition for whether num is divisible by 3
    elif num % 3 == 0:
        return "Fizz"
    
    # Define condition for whether num is divisible by both 5 
    elif num % 5 == 0:
        return "Buzz"
    
    # Return num if all conditions are false
    else:
        return num
print(fizzbuzz(45))

def calculator(operation, num1, num2):
    if operation == "+" :
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        if num2 != 0:
            return num1/num2
        else:
            return "Error: Division of a number by zero is not allowed."
    else:
        print("Invalid operation!")
        return None
print(calculator("/",2,0))