import random

def main():
    options = ['rock', 'paper', 'scissors']
    # Computer Choice
    cc = random.choice(options)

    # User Choice
    uc = input("Enter Rock, Paper, or Scissors: ").lower()
    
    if uc == "rock" or uc == "paper" or uc == "scissors":
        if cc == uc:
            print("Its a tie!")
        elif cc == "rock" and uc == "paper":
            print("You won!")
        elif cc == "rock" and uc == "scissors":
            print("You lose!")
        
    else:
        print("Invalid Option")
    

if __name__ == "__main__":
    main()