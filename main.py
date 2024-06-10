import math
class Square:
    def __init__(self, side_lenght):
        if side_lenght <=0:
            raise ValueError("Side lenght must be a positive number")
        self.side_lenght = side_lenght
    
    def calculate_perimeter(self):
        return self.side_lenght *4
    def calculate_area(self):
        return self.side_lenght**2
class Rectangle:
    def __init__(self, side_lenghtA, side_lenghtB):
        if side_lenghtA <= 0 or side_lenghtB <= 0:
            raise ValueError("Side lenght must be a positive number")
        self.side_lenghtA = side_lenghtA
        self.side_lenghtB = side_lenghtB

    def calculate_perimeter(self):
        return (self.side_lenghtB *2 ) +(self.side_lenghtA * 2)
    def calculate_area(self):
        return self.side_lenghtA * self.side_lenghtB
class Triangle_equilateral:
    def __init__ (self, side_lenght):
        if side_lenght <=0:
            raise ValueError("Side lenght must be a positive number")
        self.side_lenght = side_lenght
    def calculate_perimeter(self):
        return self.side_lenght *3
    def calculate_area(self):
        return (math.sqrt(3) / 2) * self.side_lenght
class Circle:
    def __init__ (self, radius,):
        if radius <=0:
            raise ValueError("Radius must be a pistive number")
        self.radius = radius
    def calculate_perimeter(self):
        return 2*math.pi*self.radius
    def calculate_area(self):
        return math.pi*self.radius**2

        
while True:
    print("Main menu: ")
    print("1. Square")
    print("2. Rectangle")
    print("3. Equilateral triangle")
    print("4. Circle")
    choose = input("Choose your Action: ")
    if choose == "1":
        while True:
            print("1. Circuit calculations")
            print("2. Field calculations")
            action = input("Choose your action: ")
            if action == "1":
                side_lenght = float(input("Enter the side lenght: "))
                square = Square(side_lenght)
                print("Perimeter of the square:", square.calculate_perimeter())
            elif action == "2":
                side_lenght = float(input("Enter the side lenght: "))
                square = Square(side_lenght)
                print("Area of the square: ", square.calculate_area())
            else:
                print("Error. Try Again! ")
                continue
            break
    elif choose == "2":
        while True:
            print("1. Circuit calculations")
            print("2. Field calculations")
            action = input("Chose your action: ")
            if action == "1":
                side_lenghtA = float(input("Enter the side A lenght: "))
                side_lenghtB = float(input("Enter the side B lenght: "))
                rectangle = Rectangle(side_lenghtA, side_lenghtB)
                print ("Permieter of rectangle is: ", rectangle.calculate_perimeter())
            elif action == "2":
                side_lenghtA = float(input("Enter the side A lenght: "))
                side_lenghtB = float(input("Enter the side B lenght: "))
                rectangle = Rectangle(side_lenghtA, side_lenghtB)
                print("Area of the rectangle is: ", rectangle.calculate_area())
            else:
                print ("Error. Try again!")
                continue
            break
    elif choose == "3":
        while True:
            print("1. Circuit calculations")
            print("2. Field calculations")
            action = input("Chose your action: ")
            if action == "1":
                side_lenght = float(input("Enter the side lenght: "))
                triangle = Triangle_equilateral(side_lenght)
                print("Perimeter of triangle equilateral is: ", triangle.calculate_permiter())
            elif action == "2":
                side_lenght = float(input("Enter the side lenght: "))
                triangle = Triangle_equilateral(side_lenght)
                print("Area of triangle equilateral is: ", triangle.calculate_area())
            else:
                print("Error! Try again!")
                continue
            break
    elif choose =="4":
        while True:
            print("1. Circuit calculations")
            print("2. Field calculations")
            action = input("Choose your action: ")
            if action == "1":
                radius = float(input("Type radius: "))
                circle = Circle(radius)
                print("Permiter of circle is: ", circle.calculate_perimiter())
            elif action == "2":
                radius = float(input("Type your radius:" ))
                circle = Circle(radius)
                print("Area of circle is: ", circle.calculate_area())
            else:
                print("Error! Try again!")
                continue
            break
    else:
        print("Error!Try again!")