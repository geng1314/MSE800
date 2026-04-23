import math


class Calculator:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b    

    def divide(self): 
        if self.b == 0:
            raise ValueError("Division by zero")
        return self.a / self.b


def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def menu_select():
    print("\n--- Calculator Menu choose ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide") 

if __name__ == "__main__":
    menu_select()
    choice = input("Choose an option: ")
    
    a, b = get_numbers()
    calc = Calculator(a, b)

    if choice == "1":
        print(calc.add())
    elif choice == "2":
        print(calc.subtract())
    elif choice == "3":
        print(calc.multiply())
    elif choice == "4":
        print(calc.divide())
    else:
        print("Invalid choice")



