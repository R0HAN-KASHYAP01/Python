def Area_Volume():
    operation = input("Choose the Area(A) or Volume(V): ")
# FOR AREA....
    if operation == "A" or operation == "a":
        print("Rectangle, Square, Triangle, Equilateral triangle,  Parallelogram, Trapezium, Any polygon")
        print("Choose one form any of the object")
        obj = input()
        if obj == "Rectangle" or obj == "rectangle":
            length = int(input("Enter the length: "))
            breadth = int(input("Enter the breadth: "))
            print(
                f"The area of the rectangle of length {length} and breadth {breadth} = {length*breadth} ")
        elif obj == "Square" or obj == "square":
            length = int(input("Enter the length: "))
            print(
                f"The area of the square of length {length}  = {length*length} ")
        elif obj == "Equilateral triangle" or obj == "equilateral triangle":
            length = int(input("Enter the length of a side: "))
            print(
                f"The area of the equilateral triangle of length of a side {length}= {(1/4)*(3**0.5)*(length**2)} ")
        elif obj == "Trapezium" or obj == "trapezium":
            height = int(input("Enter the height: "))
            a = int(input("Enter the length of  upper side: "))
            b = int(input("Enter the length of  lower side: "))
            print(
                f"The area of the parallelogram of height {height}, upper side {a} and lower side {b} = {(1/2)*(a+b)*(height)} ")
        elif obj == "parallelogram" or obj == "Parallelogram":
            height = int(input("Enter the height: "))
            breadth = int(input("Enter the breadth: "))
            print(
                f"The area of the rectangle of height {height} and breadth {breadth} = {height * breadth} ")
        elif obj == "Triangle" or obj == "triangle":
            height = int(input("Enter the height: "))
            breadth = int(input("Enter the breadth: "))
            print(
                f"The area of the rectangle of height {height} and breadth {breadth} = {(height * breadth)*1/2} ")
        elif obj == "Circle" or obj == "circle":
            radius = int(input("Enter the radius: "))
            print(
                f"The area of the circle of radius {radius} = {(3.14)*(radius**2)}")
        elif obj == "Any polygon" or obj == "any polygon":
            n = int(input("Enter the number of side the polygon: "))
            a = int(
                input("Enter the length of the apothem/distance between center to the side: "))
            s = int(input("Enter the length of the side: "))
            if n == 5:
                name = "Pentagon"
                print(f"The area of the {name} = {(n * a * s) / 2} ")
            elif n == 6:
                name = "Hexagon"
                print(f"The area of the {name} = {(n * a * s) / 2} ")
            elif n == 7:
                name = "Septagon"
                print(f"The area of the {name} = {(n * a * s) / 2} ")
            elif n == 8:
                name = "Octagon"
            print(f"The area of the {name} = {(n*a*s)/2} ")
        else:
            print("Sorry! Choose a valid shape")
# FOR VOLUME....
    elif operation == "V" or operation == "v":
        print("Cube, Cuboid, Sphere, Cyclinder, Cone")
        print("Choose one form any of the object")
        obj = input()
        if obj == "Cube" or obj == "cube":
            l = int(input("Enter the side of the cube: "))
            print(f"The Volume of the cube of length{l} = {l**3} ")
        elif obj == "Cuboid" or obj == "cuboid":
            l = int(input("Enter the length of the cuboid: "))
            b = int(input("Enter the breadth of the cuboid: "))
            h = int(input("Enter the height of the cuboid: "))
            print(
                f"The Volume of the cuboid of length{l}, breadth{b} and height{h} = {l*b*h}")
        elif obj == "Sphere" or obj == "sphere":
            r = int(input("Enter the radius of the sphere: "))
            print(
                f"The Volume of the sphere of radius{r} = {(4/3)*(3.14)*(r**3)} ")
        elif obj == "Cyclinder" or obj == "cyclinder":
            r = int(input("Enter the radius of the cyclinder: "))
            h = int(input("Enter the height of the cyclinder: "))
            print(
                f"The Volume of the cyclinder of radius{r} and height{h} = {(3.14)*(r**2)*(h)}")
        elif obj == "Cone" or obj == "cone":
            r = int(input("Enter the radius of the cone: "))
            h = int(input("Enter the height of the cone: "))
            print(
                f"The Volume of the cone of radius{r} and height{h} = {((3.14) * (r ** 2) * (h))/3}")
        else:
            print("Sorry! Choose a valid shape")


# FOR WRONG OPERATION....
    else:
        print("Sorry! Enter a valid operation")


Area_Volume()
# FOR Reapting the program
while True:
    Y_N = input('''Do you want to repeat it.
    If Yes (enter - Y) or No (enter - N) ''')
    if Y_N == "Y":
        Area_Volume()
    else:
        pass
        exit()

