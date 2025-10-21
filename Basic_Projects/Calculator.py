# Code on basic calculator project.
# Step 1:- Defining basic arithmatic operations.

def add (x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x/y

# Step 2: Creating central function for user input.

def get_numbers(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def calculator():
    print("Welcome to the python function calculator.")
    
    num1 = get_numbers("The first number is:- ")
    num2 = get_numbers("The second number is:- ")
    
    print("\n Available operations:")
    print(" + : Addition")
    print(" - : Substraction")
    print(" * : Multiplication")
    print(" / : Division")
    
    operation = input("choose an operation (+, -, *, /): ")
    
    result = None
    
    # Determining the operational conditionals.
    
    if operation == '+':
        result = add(num1, num2)
        
    elif operation == '-':
        result = substract(num1, num2)
        
    elif operation == '*':
        result = multiply(num1, num2)
        
    elif operation == '/':
        result = divide(num1, num2)
        
    else:
        print("Invalid operation." )
        
    
    if result is not None:
        print(f"\n Result: {num1} {operation} {num2} = {result}")
        

if __name__ == '__main__':
    calculator()