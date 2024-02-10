# Area Calculator...
print("Welcome!\nHere, you can calculate the area of circle, triangle, rectangle, square, trapezium and hexagon...")
print("Press initials of shapes for calculation.\n1.Circle\n2.Triangle\n3.Rectangle\n4.Square\n5.Trapezium\n6.Hexagon\n")
shape = int(input("Enter the type of the shape of whose area you want to calculate:-"))
match shape:
    case 1:
        rad = float(input("Enter the value of the radius of the circle: "))
        print("The area of the circle is: ", (3.14*rad*rad))

    case 2:
        base = float(input("Enter the value of the base of the triangle: "))
        height = float(input("Enter the value of the: "))
        print("The area of the triangle is: ", (base*height)/2)

    case 3:
        length = float(input("Enter the value of the length of the rectangle: "))
        width = float(input("Enter the value of the width of the rectangle: "))
        print("The area of the rectangle is: ", length*width)

    case 4:
        side = float(input("Enter the value of the side of the square: "))
        print("The area of the square is: ", side*side)

    case 5:
        base = float(input("Enter the value of the base of the trapezium: "))
        top = float(input("Enter the value of the top of the trapezium: "))
        height = float(input("Enter the value of the height of the trapezium: "))
        print("The area of the trapezium is: ", ((base + top) * height)/2)

    case 6:
        side = float(input("Enter the value of the side of the Hexagon: "))
        print("The area of the hexagon is: ", ((3*1.732)/2) * side * side)

    case _:
        print("Invalid")
