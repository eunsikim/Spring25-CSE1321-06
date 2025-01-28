# triangle, quadrilateral, pentagon, 
# hexagon, or “I do not know a 
# shape with that many sides”

def main():
    isShape = False
    userInput = int(input("How manny sides does your shape have: "))

    match userInput:
        case 3:
            print("You have a triangle")
            isShape = True
        case 4:
            print("You have a quadrilateral")
            isShape = True
        case 5:
            print("You have a pentagon")
            isShape = True
        case 6:
            print("You have a hexagon")
            isShape = True
        case _:
            print("I do not know a shape with that many sides")
    
    if isShape: # if isShape == True
        side = int(input("What is the length of all sides: "))

        print(f"Perimeter = {side * userInput}")

if __name__ == "__main__":
    main()