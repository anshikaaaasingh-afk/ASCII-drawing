def draw_line(length):
    print("*" * length)

def draw_rectangle(width, height):
    for _ in range(height):
        print("*" * width)

def draw_hollow_rectangle(width, height):
    for row in range(height):
        if row == 0 or row == height - 1:
            print("*" * width)
        else:
            print("*" + " " * (width - 2) + "*")

def draw_square(size):
    draw_rectangle(size, size)

def draw_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

def draw_pyramid(height):
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

def draw_canvas(width, height):
    for _ in range(height):
        print("." * width)

while True:
    print("\n=== ASCII DRAWING TOOL ===")
    print("1. Draw Line")
    print("2. Draw Rectangle")
    print("3. Draw Hollow Rectangle")
    print("4. Draw Square")
    print("5. Draw Triangle")
    print("6. Draw Pyramid")
    print("7. Draw Canvas")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        length = int(input("Length: "))
        draw_line(length)

    elif choice == "2":
        width = int(input("Width: "))
        height = int(input("Height: "))
        draw_rectangle(width, height)

    elif choice == "3":
        width = int(input("Width: "))
        height = int(input("Height: "))
        draw_hollow_rectangle(width, height)

    elif choice == "4":
        size = int(input("Size: "))
        draw_square(size)

    elif choice == "5":
        height = int(input("Height: "))
        draw_triangle(height)

    elif choice == "6":
        height = int(input("Height: "))
        draw_pyramid(height)

    elif choice == "7":
        width = int(input("Canvas Width: "))
        height = int(input("Canvas Height: "))
        draw_canvas(width, height)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
        