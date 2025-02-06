def main():
    x = 0
    while x < 3:
        print("Outer Loop")
        y = 0
        while y < 2:
            print("\tInner Loop")
            y += 1
        x+= 1

if __name__ == "__main__":
    main()