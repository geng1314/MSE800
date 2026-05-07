# main.py
from rectangle import Rectangle

def main():
    print("Rectangle Area and Perimeter Calculator")
     
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
 
    rect = Rectangle(length, width)
 
    area = rect.calculate_area()
    perimeter = rect.calculate_perimeter()
 
    print("Area:", area)
    
    print("Perimeter:", perimeter)

if __name__ == "__main__":
    main()