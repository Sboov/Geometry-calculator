import math

while True:
    print("Main menu: ")
    print("1. Square")
    print("2. Rectangle")
    print("3. Equilateral triangle")
    print("4. Exit")  
    choose = input("Choose your geometry figure: ")

    if choose == '1':
        while True:  
            print("Choose your action:")
            print("1. Circuit calculations")
            print("2. Field calculations")
            print("3. Back to main menu")
            action = input("Choose your action: ")
            if action == '1':
                a = int(input("Type the side length: "))
                square_circut = a * 4
                print("Square circuit is: ", square_circut)
            elif action == '2':
                a = int(input("Type the side length: "))
                square_field = a ** 2
                print("Square field is: ", square_field)
            elif action == '3':
                break  
            else:
                print("Wrong action. Try again!")
                
    elif choose == '2':
        while True: 
            print("Choose your action:")
            print("1. Circuit calculations")
            print("2. Field calculations")
            print("3. Back to main menu")
            action = input("Choose your action: ")
            if action == "1":
                a = int(input("Type the first side length: "))
                b = int(input("Type the second side length: "))
                rectangle_circuit = (2 * a) + (2 * b)
                print("Rectangle circuit is: ", rectangle_circuit)
            elif action == "2":
                a = int(input("Type the first side length: "))
                b = int(input("Type the second side length: "))
                rectangle_field = a * b
                print("Rectangle field is: ", rectangle_field)
            elif action == "3":
                break  
            else:
                print("Wrong action. Try again!")
                
    elif choose == '3':
        while True:  
            print("Choose your action:")
            print("1. Circuit calculations")
            print("2. Field calculations")
            print("3. Back to main menu")
            action = input("Choose your action: ")
            if action == "1":
                a = int(input("Type the side length: "))
                equilateral_triangle = a * 3
                print("Circuit of equilateral triangle is: ", equilateral_triangle)
            elif action == "2":
                a = int(input("Type the side length: "))
                equilateral_triangle_field = (a ** 2 * math.sqrt(3)) / 4
                print("Field of equilateral triangle is: ", equilateral_triangle_field)
            elif action == "3":
                break  
            else:
                print("Wrong action. Try again!")
                
    elif choose == '4':
        break  
    else:
        print("Wrong action. Try again!")