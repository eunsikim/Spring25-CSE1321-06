def main():
    count = int(input("Enter a number: "))

    for i in range(1, count + 1): # count = 5 therefore i [1, 4]
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end="") 
        elif i % 3 == 0: # i is divisible by 3
            print("Fizz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        else:
            print(i, end="")
        
        
        print(f"{'' if i == count else ', '}" , end="")
        
        
        

if __name__ == "__main__":
    main()