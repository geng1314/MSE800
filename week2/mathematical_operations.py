import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b    

def divide(a, b): 
    if b == 0:
        raise ValueError("Division by zero ")
    return a / b

def power(a, b):
    return math.pow(a, b)

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    
    print("num1 = 10, num2 = 5")
    print("add:", add(num1, num2))
    print("subtract:", subtract(num1, num2))
    print("multiply:", multiply(num1, num2))
    print("divide:", divide(num1, num2))
    print("power:", power(num1, num2))



