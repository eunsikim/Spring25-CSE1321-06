def printSquare(size):
    if size < 3:
        print("You need to enter a size greater than or equal to 3!")
        return False
    
    for row in range(size):
        for col in range(size):
            if row == 0 or row == size - 1:
                print("-", end = "")
            else:
                if col == 0 or col == size - 1:
                    print("|", end = "")
                else:
                    print(" ", end = "")
        print()
    
    return True


def main():
    while True:
        size = int(input("Enter a size: ")) 
        
        if printSquare(size):
            break

if __name__ == "__main__":
    main()