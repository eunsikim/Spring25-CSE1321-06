# Find a way to finish the game
#   Maybe we need to add a break after
#   we found out who the winner is

def main():
    grid = [
        ["", "", ""], 
        ["", "", ""], 
        ["", "", ""]]

    while True:
        player1ActionRow = int(input("Where do you want to add an X (Row): "))
        player1ActionCol = int(input("Where do you want to add an X (Col): "))

        grid[player1ActionRow][player1ActionCol] = "X"

        for row in grid:
            for col in row:
                print(f"|{col}|", end="")
            print()

        player2ActionRow = int(input("Where do you want to add an O (Row): "))
        player2ActionCol = int(input("Where do you want to add an O (Col): "))

        grid[player2ActionRow][player2ActionCol] = "O"

        for row in grid:
            for col in row:
                print(f"|{col}|", end="")
            print()

if __name__ == "__main__":
    main()